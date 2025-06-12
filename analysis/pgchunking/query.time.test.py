import random
import subprocess
import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-n', help='number of regions', type=int, default=10)
parser.add_argument('-s', help='size of regions', type=int, default=500)
parser.add_argument('-r', help='reference path only', action='store_true')
args = parser.parse_args()

# read contig lengths
inf = open('contig.lengths.txt', 'rt')
contig_size = {}
for line in inf:
    line = line.rstrip().split('\t')
    if '_' in line[0]:
        # skip alt contigs
        continue
    if 'GRCh38' not in line[0] and args.r:
        continue
    contig_size[line[0]] = int(line[1])
inf.close()

# sample n regions of size s bp
reg_chunkix = []
reg_vgchunk = []
nregion = 0
while nregion < args.n:
    chr_s = random.randint(0, len(contig_size) - 1)
    chr_s = list(contig_size.keys())[chr_s]
    chr_s_vgc = chr_s
    csize = contig_size[chr_s]
    first_pos = 0
    if '[' in chr_s:
        # if in the form CONTIG[OFFSET] we're dealing with a subpath
        # i.e. a piece of the CONTIG path starting at OFFSET
        first_pos = int(chr_s.replace(']', '').split('[')[1])
        chr_s = chr_s.split('[')[0]
        chr_s_vgc = chr_s
    if len(chr_s.split('#')) == 4:
        # if in the form CONTIG#OFFSET we're dealing with a subpath
        # i.e. a piece of the CONTIG path starting at OFFSET
        chr_s = chr_s.split('#')
        first_pos = int(chr_s[3])
        chr_s = '#'.join(chr_s[:3])
    last_pos = first_pos + csize - 1 - args.s
    if last_pos > first_pos:
        # it's possible to get a region of length args.s in that contig
        pos_s = random.randint(first_pos, last_pos)
        reg_chunkix.append('{}:{}-{}'.format(chr_s, pos_s, pos_s + args.s))
        reg_vgchunk.append('{}:{}-{}'.format(chr_s_vgc, pos_s, pos_s + args.s))
        nregion += 1

# print header of output TSV
print('region\ts\tmethod\tcmd')

# query with chunkix.py
nodes_fn = 'hprc-v1.1-mc-grch38.nodes.tsv.gz'
pos_fn = 'hprc-v1.1-mc-grch38.pos.bed.gz'
haps_fn = 'hprc-v1.1-mc-grch38.haps.gaf.gz'
for reg_n in reg_chunkix:
    cmd = ['python3', 'chunkix.py', '-p', pos_fn, '-n', nodes_fn,
           '-g', haps_fn, '-r', reg_n, '-o', 'temp', '-s']
    t_s = datetime.datetime.now()
    subprocess.run(cmd, check=True, capture_output=True)
    t_e = datetime.datetime.now()
    dur = t_e - t_s
    print('{}\t{}\tchunkix\t{}'.format(reg_n,
                                       dur.total_seconds(),
                                       ' '.join(cmd)))

# query with chunkix.py on remote index files
nodes_fn = 'https://public.gi.ucsc.edu/~jmonlong/sequencetubemap_tabix/hprc.nodes.tsv.gz'
pos_fn = 'https://public.gi.ucsc.edu/~jmonlong/sequencetubemap_tabix/hprc.pos.bed.gz'
haps_fn = 'https://public.gi.ucsc.edu/~jmonlong/sequencetubemap_tabix/hprc.haps.gaf.gz'
for reg_n in reg_chunkix:
    cmd = ['python3', 'chunkix.py', '-p', pos_fn, '-n', nodes_fn,
           '-g', haps_fn, '-r', reg_n, '-o', 'temp', '-s']
    t_s = datetime.datetime.now()
    subprocess.run(cmd, check=True, capture_output=True)
    t_e = datetime.datetime.now()
    dur = t_e - t_s
    print('{}\t{}\tchunkix_remote\t{}'.format(reg_n,
                                              dur.total_seconds(),
                                              ' '.join(cmd)))

# query with vg chunk
gbz_fn = 'hprc-v1.1-mc-grch38.gbz'
for reg_n in reg_vgchunk:
    cmd = ['vg', 'chunk', '-c', '1', '-x', gbz_fn, '-p', reg_n,
           '-T', '-t', '1']
    # print(' '.join(cmd))
    t_s = datetime.datetime.now()
    cmd_o = subprocess.run(cmd, capture_output=True)
    t_e = datetime.datetime.now()
    dur = t_e - t_s
    if cmd_o.returncode != 0:
        dur = 'NA'
    else:
        dur = dur.total_seconds()
    print('{}\t{}\tvg\t{}'.format(reg_n, dur,
                                  ' '.join(cmd)))
