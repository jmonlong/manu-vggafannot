import argparse
import subprocess
import os


def parsePath(path_raw):
    cur_node = ''
    cur_orient = ''
    path = []
    fwd_diff = 0
    for ii in range(len(path_raw)):
        if path_raw[ii] == '<' or path_raw[ii] == '>':
            if cur_node != '':
                path.append([cur_node, cur_orient])
            cur_orient = path_raw[ii] == '>'
            if cur_orient:
                fwd_diff += 1
            else:
                fwd_diff += -1
            cur_node = ''
        else:
            cur_node += path_raw[ii]
    if cur_node != '':
        path.append([cur_node, cur_orient])
    return (path)


parser = argparse.ArgumentParser('Prepare a subgraph and annotations'
                                 ' for Bandage')
parser.add_argument('-g', help='pangenome in a VG format, e.g. .gbz or .pg',
                    required=True)
parser.add_argument('-a', default=[], action='append',
                    help='optional annotations, in bgzipped and indexed'
                    ' GAF files. Can repeat')
parser.add_argument('-p', help='path coordinates', required=True)
parser.add_argument('-c', help='additional node context to extract',
                    default=20, type=int)
parser.add_argument('-o', help='output prefix', default='chunk')
args = parser.parse_args()


# run vg chunk to get a slice of the pangenome and annotations
cmd = ['vg', 'chunk', '-x', args.g, '-c', str(args.c), '-p', args.p]
# add annotations
temp_prefix = args.o + '.temp'
if len(args.a):
    cmd += ['-g', '-F', '-b', temp_prefix]
    for afn in args.a:
        cmd += ['-a', afn]
# redirect output to this temporary file
temp_pg = args.o + '.temp.pg'
outf = open(temp_pg, 'w')
print("Running: {}".format(' '.join(cmd)))
cmd_o = subprocess.run(cmd, check=True, stdout=outf)
outf.close()

# Convert to GFA
cmd = ['vg', 'view', temp_pg]
print("Running: {}".format(' '.join(cmd)))
cmd_o = subprocess.run(cmd, check=True, capture_output=True)
# write GFA, making sure the paths are last
out_gfa_fn = args.o + '.gfa'
outf = open(out_gfa_fn, 'wt')
# to save path names and nodes in the subgraph
gfa_paths = []
nodes = {}
# read the GFA output stream from vg view
for line in cmd_o.stdout.decode().rstrip().split('\n'):
    line_v = line.rstrip().split('\t')
    # save node ID
    if line_v[0] == 'S':
        nodes[line_v[1]] = True
    # save paths for later, Bandage prefers when they're last
    if line_v[0] == 'P':
        gfa_paths.append(line)
        continue
    # other write as is
    outf.write(line + '\n')
# write the paths last
for line in gfa_paths:
    outf.write(line + '\n')
outf.close()
print("Wrote GFA: {}".format(out_gfa_fn))

# list GAF files
if len(args.a):
    gaf_fns = []
    for fn in os.listdir():
        if fn.startswith(temp_prefix) and fn.endswith('.gaf'):
            gaf_fns.append(fn)

    print("Preparing GAF(s): {}".format(' '.join(gaf_fns)))
    # make a unique GAF file
    out_gaf_fn = args.o + '.gaf'
    out_gaf = open(out_gaf_fn, 'wt')
    path_names = {}
    for gaf_fn in gaf_fns:
        in_gaf = open(gaf_fn, 'rt')
        for line in in_gaf:
            line = line.rstrip().split('\t')
            # make sure path names are unique
            if line[0] in path_names:
                path_names[line[0]] += 1
                line[0] = '{}_{}'.format(line[0],
                                         path_names[line[0]])
            # save path names to avoid duplicates later
            path_names[line[0]] = 1
            # we might need to modify the path
            # e.g. if it contains nodes not in the extracted subgraph
            # (BandageNG doesn't like that)
            path = parsePath(line[5])
            # trim paths with missing nodes
            path_beg = 0
            while path[path_beg][0] not in nodes and path_beg < len(path) - 1:
                path_beg += 1
            path_end = len(path) - 1
            while path[path_end][0] not in nodes and path_end > 0:
                path_end += -1
            path_end += 1
            path = path[path_beg:path_end]
            # skip paths still containing a missing node?
            skip = len(path) == 0
            for no in path:
                if no[0] not in nodes:
                    skip = True
            # write GAF record
            if not skip:
                path_string = ''
                for no in path:
                    path_string += ['<', '>'][no[1]] + no[0]
                line[5] = path_string
                out_gaf.write('\t'.join(line) + '\n')
        in_gaf.close()
    out_gaf.close()
    print("Wrote GAF: {}".format(out_gaf_fn))

# remove temporary files
cmd = ['rm', temp_pg] + gaf_fns
print("Running: {}".format(' '.join(cmd)))
cmd_o = subprocess.run(cmd, check=True)
