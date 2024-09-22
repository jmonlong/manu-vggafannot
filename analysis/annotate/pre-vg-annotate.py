import argparse
import gzip


parser = argparse.ArgumentParser(description="Prepare files before"
                                 " vg annotate")
parser.add_argument('-i', help='input file', required=True)
parser.add_argument('-t', default='bed',
                    help='type of file: bed (default) or gff3')
parser.add_argument('--use-name-id', dest="name_id", action='store_true',
                    help='in GFF3, change Name to be <Name>:<ID>. '
                    'Implies: -t gff3')
parser.add_argument('--add-prefix', dest="add_pref", default="",
                    help='add provided prefix to sequence names')
parser.add_argument('--add-suffix', dest="add_suff", default="",
                    help='add provided suffix to record names')
parser.add_argument('--add-rep-n', dest="add_rep_n", action="store_true",
                    help='name record as (<MOTIF>)<N> in TRF BED')
parser.add_argument('--add-len-fracm', dest="add_len_fracm",
                    action="store_true",
                    help='name record as <LENGTH>bp_<FRACMATCH> for segdups'
                    ' in SEDEF output')
parser.add_argument('--add-rm-class', dest="add_rm_class",
                    action="store_true",
                    help='prefix repeat name with its class'
                    ' in RepeatMasker output')

args = parser.parse_args()

# guess if it's a gzipped file
in_gzip = True
with gzip.open(args.i, 'rb') as inf:
    try:
        inf.read(1)
    except OSError:
        in_gzip = False

# open input file
if in_gzip:
    inf = gzip.open(args.i, 'rt')
else:
    inf = open(args.i, 'rt')

# init column numbers for copy number and motif in TRF output
# will also look in the header later just in case
cn_idx = 4
motif_idx = 14
# init column numbers for aln_len and fracMatch in SEDEF output
# (https://github.com/vpc-ccg/sedef#output)
len_idx = 11
fracm_idx = 21

# read input one line at a time
for line in inf:
    line = line.rstrip()
    # if starts with a comment character, nothing to do
    if line[0] == '#':
        # check just in case if a column is called "CopyNumber" or "Motif"
        line = line.split('\t')
        for ii in range(len(line)):
            if line[ii] == 'CopyNumber':
                cn_idx = ii
            elif line[ii] == "Motif":
                motif_idx = ii
        if args.add_rep_n:
            # add header for the new "name" column
            line = line[:3] + ["name"] + line[3:]
        # print line
        print('\t'.join(line))
        continue
    # otherwise parse tab-separated line
    line = line.rstrip().split('\t')
    ## rename "Name" in GFF3 to be "Name:ID"
    if args.name_id:
        new_name = ':'
        name_idx = -1
        gff_infos = line[8].split(';')
        for ii in range(len(gff_infos)):
            gff_info = gff_infos[ii].split('=')
            if gff_info[0] == 'Name':
                new_name = gff_info[1] + new_name
                name_idx = ii
            if gff_info[0] == 'ID':
                new_name = new_name + gff_info[1]
        gff_infos[name_idx] = "Name=" + new_name
        line[8] = ';'.join(gff_infos)
    # remove prefix from sequence names (first column)
    if args.add_pref != "":
        line[0] = args.add_pref + line[0]
    # rename TRF bed to (MOTIF)N
    if args.add_rep_n:
        new_col = '({}){}'.format(line[motif_idx],
                                  int(float(line[cn_idx])))
        line = line[:3] + [new_col] + line[3:]
    # rename SEDEF bed to LENGTH_FRACMATCH
    if args.add_len_fracm:
        new_col = '{}bp_{}'.format(line[len_idx],
                                   round(float(line[fracm_idx]), 3))
        line = line[:3] + [new_col] + line[3:]
    # prefix fourth column with repeatClass value for repeatmasker
    if args.add_rm_class:
        line[3] = '{}|{}'.format(line[6], line[3])
    # add suffix if specified
    if args.add_suff != '':
        if args.t == 'gff3':
            gff_infos = line[8].split(';')
            for ii in range(len(gff_infos)):
                gff_info = gff_infos[ii].split('=')
                if gff_info[0] == 'Name':
                    new_name = gff_info[1] + args.add_suff
                    line[ii] = 'Name={}'.format(new_name)
        elif args.t == 'bed':
            line[3] = line[3] + args.add_suff
        else:
            print("only bed and gff3 accepted as file type (-t).")
    # print updated record
    print('\t'.join(line))

# close input file
inf.close()
