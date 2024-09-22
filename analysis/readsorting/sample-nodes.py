import random
import fileinput


# expect a GAF stream. for example use with:
# vg paths -x hprc-v1.1-mc-grch38.gbz -A -Q GRCh38 | python3 sample-nodes.py > random-node-intervals.bed

# how many node intervals
N = 10000
# how long are the intervals
L = 50

# list of list of nodes
# one list per chromosome/path
paths = []
path_lens = []
for line in fileinput.input():
    path = line.split('\t')[5].replace('>', '<').split('<')
    paths.append(path[1:])
    path_lens.append(len(path) - 1)

# sample a chromosome and then a node position
path_iis = list(range(len(path_lens)))
samp_seqis = random.sample(path_iis, N, counts=path_lens)
for seqi in samp_seqis:
    node_start = random.randint(0, len(paths[seqi]) - L)
    node_end = node_start + L - 1
    print('{{n}}:{}-{}'.format(paths[seqi][node_start], paths[seqi][node_end]))
