import argparse
import gzip
import bdsg


parser = argparse.ArgumentParser('Extract variants from VCF and make paths')
parser.add_argument('-g', help='pangenome graph file', required=True)
parser.add_argument('-p', help='pangenome VCF', required=True)
parser.add_argument('-v', help='variant information', required=True)
parser.add_argument('-s', help='source of the variants', required=True)
parser.add_argument('-o', help='output GAF file', required=True)
parser.add_argument('-l', help='label to add to path name', default='')
args = parser.parse_args()

# read variant information


def prepareInfoGWAS(line):
    # gwas files have columns: 2 chr, 3/4 start/end, 11 trait, 16 risk allele
    if line[1] == '':
        return (('', ''))
    # variant ID to save and match with VCF later
    var_id = '{}_{}'.format(line[1].replace('chr', ''), line[3])
    # extract risk allele
    if '-' not in line[15] or '-?' in line[15]:
        riskalt = ''
    else:
        riskalt = line[15].split('-')[1]
    # make a label (future path name)
    label = '{}_{}_{}'.format(line[15], line[10], var_id)
    if args.l != '':
        label = args.l + '_' + label
    # remove spaces and other symbols
    label = label.replace(' ', '-').replace(',', '-')
    label = label.replace(';', '-').replace(':', '-')
    label = label.replace(')', '-').replace('(', '-')
    label = label.replace('/', '-').replace('.', '-')
    label = label.replace("'", '').replace('|', '-')
    label = label.replace('--', '-').replace('--', '-')
    label = label.replace('-?', '').replace('-_', '_')
    # save info
    return ((var_id, {'ref': '', 'alt': riskalt, 'label': label}))


def prepareInfoGTEx(line):
    # gwas files have columns: 1 variant id, 2 gene id, 8 slope
    if line[0] == '':
        return (('', ''))
    var_d_v = line[0].split('_')
    # variant ID to save and match with VCF later
    var_id = '{}_{}'.format(var_d_v[0].replace('chr', ''), var_d_v[1])
    # make a label (future path name)
    label = '{}_{}_{}'.format(line[1], round(float(line[7]), 2), var_id)
    if args.l != '':
        label = args.l + '_' + label
    # save info
    return ((var_id, {'ref': var_d_v[2], 'alt': var_d_v[3], 'label': label}))


# dict to associate CHR_POS to an array of
# variant information (REF, ALT, metadata)
var_info = {}
skipped_var = 0
saved_var = 0

# open text file
if args.v.endswith('.gz'):
    var_in = gzip.open(args.v, 'rt')
else:
    var_in = open(args.v, 'rt')

for line in var_in:
    line = line.rstrip().split('\t')
    if args.s == 'gwas_catalog':
        vid, vinfo = prepareInfoGWAS(line)
    if args.s == 'gtex_eqtls':
        if line[0] == 'variant_id':
            continue
        vid, vinfo = prepareInfoGTEx(line)
    if vid != '':
        if vid not in var_info:
            var_info[vid] = []
        var_info[vid].append(vinfo)
        saved_var += 1
    else:
        skipped_var += 1
        print(line)
var_in.close()

print('Read information about {} variants.'.format(saved_var))
print('Skipped {} variants with missing information.'.format(skipped_var))

# load pangenome
pg = bdsg.bdsg.PackedGraph()
pg.deserialize(args.g)


def getNodeSize(node, pg):
    if pg.has_node(int(node)):
        node_h = pg.get_handle(int(node))
        return (pg.get_length(node_h))
    else:
        return (0)


# read through the pangenome VCF and look for those variants
if args.p.endswith('.gz'):
    pg_in = gzip.open(args.p, 'rt')
else:
    pg_in = open(args.p, 'rt')

outf = open(args.o, 'tw')
match_alt = 0
tot = 0
for line in pg_in:
    # skip headers
    if line[0] == "#":
        continue
    # otherwise, parse the file
    line = line.rstrip().split('\t')
    # check if position matches something
    vid = '{}_{}'.format(line[0].replace('chr', ''), line[1])
    if vid not in var_info:
        continue
    # if yes, extract the path information
    at = ''
    for info_f in line[7].split(';'):
        info_f = info_f.split('=')
        if info_f[0] == 'AT':
            at = info_f[1].split(',')
    # pick a path: alt if ALT info is there and matches, ref otherwise
    alts = line[4].split(',')
    for var in var_info[vid]:
        if var['alt'] != '' and var['alt'] in alts:
            # pick the path for the appropriate ALT allele
            path = at[alts.index(var['alt']) + 1]
            match_alt += 1
        else:
            # pick the path for the REF allele
            path = at[0]
        # prepare GAF output
        gaf_v = var['label']
        # path should start on the last base of the first node
        # and end at the first base of the last node
        path_v = path.replace('>', ',').replace('<', ',').split(',')[1:]
        full_path_len = getNodeSize(path_v[0], pg)
        if full_path_len == 0:
            continue
        offset = full_path_len - 1
        path_len = 1
        for node in path_v[1:]:
            nsize = getNodeSize(node, pg)
            if nsize == 0:
                continue
            path_len += nsize
            full_path_len += nsize
        path_len = path_len - nsize + 1
        # path length/start/end/strand
        gaf_v += '\t{}\t0\t{}\t+'.format(path_len, path_len)
        # path information: string representation and length
        gaf_v += '\t{}\t{}'.format(path, full_path_len)
        gaf_v += '\t{}\t{}'.format(offset, path_len + offset)
        # residues matching, alignment block size, and mapping quality
        gaf_v += '\t{}\t{}\t60'.format(path_len, path_len)
        outf.write(gaf_v + '\n')
        tot += 1

pg_in.close()
outf.close()

print('{} variants converted, inc. {} with '
      'matched ALT allele.'.format(tot, match_alt))
