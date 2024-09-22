import argparse
import gzip
import bdsg


parser = argparse.ArgumentParser('Extract variants from VCF and make paths')
parser.add_argument('-g', help='pangenome graph file', required=True)
parser.add_argument('-v', help='variant information', required=True)
parser.add_argument('-o', help='output GAF file', required=True)
args = parser.parse_args()

# load pangenome
pg = bdsg.bdsg.PackedGraph()
pg.deserialize(args.g)


def getNodeSize(node, pg):
    if not pg.has_node(int(node)):
        print('No node {} in pangenome?'.format(node))
        exit(1)
    node_h = pg.get_handle(int(node))
    node_size = pg.get_length(node_h)
    if node_size == 0:
        print('Node {} has length 0?'.format(node))
        exit(1)
    return (node_size)


def makeGAFrecord(path, rname, pg):
    gaf_v = rname
    # path should start on the last base of the first node
    # and end at the first base of the last node
    path_v = path.replace('>', ',').replace('<', ',').split(',')[1:]
    full_path_len = getNodeSize(path_v[0], pg)
    offset = full_path_len - 1
    path_len = 1
    for node in path_v[1:]:
        nsize = getNodeSize(node, pg)
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
    # cigar string
    gaf_v += '\tcs:Z::{}\tAS:i:{}'.format(path_len, path_len)
    return (gaf_v)


# open VCF file
if args.v.endswith('.gz'):
    var_in = gzip.open(args.v, 'rt')
else:
    var_in = open(args.v, 'rt')
outf = open(args.o, 'tw')

for line in var_in:
    if line[0] == '#':
        # skip headers
        continue
    line = line.rstrip().split('\t')
    # get a variant ID
    vid = line[2]
    # extract the path information
    at = ''
    for info_f in line[7].split(';'):
        info_f = info_f.split('=')
        if info_f[0] == 'AT':
            at = info_f[1].split(',')
    # find the genotype of the first sample
    gt_pos = line[8].split(':').index('GT')
    gt = line[9].split(':')[gt_pos]
    gt = gt.replace('|', '/').split('/')
    # make one path for each allele
    gaf_v = ''
    prev_al = ''
    for alid in range(len(gt)):
        if gt[alid] != '.':
            if gt[alid] != prev_al:
                # in case we had already prepared that allele (e.g. homozygous)
                path = at[int(gt[alid])]
                gaf_v = makeGAFrecord(path, vid, pg)
                prev_al = gt[alid]
            if gaf_v != '':
                outf.write(gaf_v + '\n')

var_in.close()
outf.close()
