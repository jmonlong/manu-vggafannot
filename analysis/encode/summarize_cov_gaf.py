import fileinput


# python script to tally the number of regions in the coverage track
# with each profile of coverage/node length/basepair length.

# tally the counts in this dict
# "coverage_bin n_node n_bp" -> number of regions
regs = {}

# parse the GAF output
for line in fileinput.input():
    line = line.rstrip().split('\t')
    # get number of nodes in the path
    path = line[5].replace('>', '<').split('<')[1:]
    nnodes = len(path)
    # get number of bases
    nbp = int(line[1])
    # get mean coverage
    cid = line[0].split('_')
    cov_bin = round(float(cid[3]))
    # prepare profile (coverage bin, n nodes, n bp)
    regi = '{}\t{}\t{}'.format(cov_bin, nnodes, nbp)
    # increment counts for this profile
    if regi not in regs:
        regs[regi] = 0
    regs[regi] += 1

# write counts for each profile
print('coverage_bin\tn_node\tn_bp\tn')
for regi in regs:
    print(regi + '\t' + str(regs[regi]))
