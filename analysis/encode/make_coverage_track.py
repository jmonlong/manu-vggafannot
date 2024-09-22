import argparse
import bdsg
import fileinput
import sys


class Node:
    def __init__(self, id, cov_arr=[], full_len=0):
        self.id = id
        self.cov_len = []
        self.cov_val = []
        self.full_len = full_len
        self.bin = ''
        self.offset = 0
        self.flag = False
        self.flank_start = True
        self.flank_end = True
        if len(cov_arr) > 0:
            self.updateCoverage(cov_arr)

    def updateCoverage(self, cov_arr):
        cur_val = cov_arr[0]
        cur_len = 1
        for val in cov_arr[1:]:
            if val == cur_val:
                cur_len += 1
            else:
                self.cov_val.append(cur_val)
                self.cov_len.append(cur_len)
                cur_val = val
                cur_len = 1
        if cur_len > 0:
            self.cov_val.append(cur_val)
            self.cov_len.append(cur_len)

    def binCoverage(self, cov_breaks):
        # binned nodes to return
        bnodes = []
        # parent node full length
        full_len = self.getLength()
        # breaks of the current coverage bin
        min_cov = -1
        max_cov = cov_breaks[0]
        # current coverage bin
        cur_cov_len = []
        cur_cov_val = []
        # to keep track of our position in the node
        offset = 0
        # bin the coverage track of the node
        for covii in range(len(self.cov_len)):
            # are we in the same coverage bin?
            if self.cov_val[covii] < max_cov and \
               self.cov_val[covii] >= min_cov:
                # yes: extend bin
                cur_cov_len.append(self.cov_len[covii])
                cur_cov_val.append(self.cov_val[covii])
            else:
                # no: create a new node
                if len(cur_cov_len) > 0:
                    nnode = Node(self.id, full_len=full_len)
                    nnode.bin = '{}_{}'.format(min_cov, max_cov)
                    nnode.offset = offset
                    nnode.cov_len = cur_cov_len
                    nnode.cov_val = cur_cov_val
                    if offset != 0:
                        # not the first bin in the node
                        nnode.flank_start = False
                    # if within this loop, not the last bin in the node
                    nnode.flank_end = False
                    bnodes.append(nnode)
                    # update the position offset within the node
                    for offs in cur_cov_len:
                        offset += offs
                # update current coverage bin
                cur_cov_len = [self.cov_len[covii]]
                cur_cov_val = [self.cov_val[covii]]
                if self.cov_val[covii] < cov_breaks[0]:
                    min_cov = -1
                    max_cov = cov_breaks[0]
                elif self.cov_val[covii] >= cov_breaks[-1]:
                    min_cov = cov_breaks[-1]
                    max_cov = 10000
                else:
                    for ii in range(len(cov_breaks)):
                        if self.cov_val[covii] < cov_breaks[ii]:
                            min_cov = cov_breaks[ii - 1]
                            max_cov = cov_breaks[ii]
                            break
        # finish the last bin
        if len(cur_cov_len) > 0:
            nnode = Node(self.id, full_len=full_len)
            nnode.bin = '{}_{}'.format(min_cov, max_cov)
            nnode.offset = offset
            nnode.cov_len = cur_cov_len
            nnode.cov_val = cur_cov_val
            if offset != 0:
                # not the first bin in the node
                nnode.flank_start = False
            bnodes.append(nnode)
        return (bnodes)

    def getMaxCoverage(self):
        max_cov = self.cov_val[0]
        for cov in self.cov_val:
            max_cov = max(max_cov, cov)
        return (max_cov)

    def getCoverageSum(self):
        cov_sum = 0
        for ii in range(len(self.cov_val)):
            cov_sum += self.cov_val[ii] * self.cov_len[ii]
        return (cov_sum)

    def getLength(self):
        return (sum(self.cov_len))


def getNextNodes(pg, node_id, forward=True):
    node = pg.get_handle(int(node_id), not forward)
    next_nodes = []

    def addToNextNodes(nhandle):
        next_nodes.append([pg.get_id(nhandle),
                           not pg.get_is_reverse(nhandle)])
        return (True)
    pg.follow_edges(node, False, addToNextNodes)
    return (next_nodes)


def extendPath(path, bnodes, forward=True, debug_mode=False):
    # init coverage stats
    cov_total = 0
    # init current node
    path_pos = 0
    if forward:
        path_pos = -1
    # get the starting Node object
    cnode = bnodes[path[path_pos][0]]
    # current node direction of traversal
    if forward:
        corient_fwd = path[path_pos][1]
    else:
        corient_fwd = not path[path_pos][1]
    # should we try to extend more? multiple cases when we should
    # we're extending forward and we're at the last bin of a node
    extend_more = corient_fwd and cnode.flank_end
    # we're extending backward and we're at the first bin of a node
    extend_more = extend_more or (not corient_fwd and cnode.flank_start)
    # extend as long as current node is the "end" of a node
    while extend_more:
        if debug_mode:
            print('\tcurrent node: {} ({})'.format(cnode.id, corient_fwd),
                  file=sys.stderr)
        # get next nodes, going in the current orientation
        nnodes_ids = getNextNodes(pg, cnode.id, corient_fwd)
        if debug_mode:
            print('\t\tnext nodes: {}'.format(nnodes_ids), file=sys.stderr)
        # find a candidate next node
        nbin_id_or = []
        for nnodeid_or in nnodes_ids:
            nnode_id = nnodeid_or[0]
            if nnodeid_or[1]:
                # we'd traverse this node forward
                # find the first bin of that node
                if nnode_id not in first_bin:
                    # skip (for now) if we don't have coverage info
                    if debug_mode:
                        print('\t\t{} not first bin'.format(nnode_id),
                              file=sys.stderr)
                    continue
                nnode_bid = first_bin[nnode_id]
            else:
                # we'd traverse this node backward
                # find the last bin of that node
                if nnode_id not in last_bin:
                    # skip (for now) if we don't have coverage info
                    if debug_mode:
                        print('\t\t{} not last bin'.format(nnode_id),
                              file=sys.stderr)
                    continue
                nnode_bid = last_bin[nnode_id]
            # skip if already part of a path
            if bnodes[nnode_bid].flag:
                if debug_mode:
                    print('\t\t{} already done'.format(nnode_bid),
                          file=sys.stderr)
                continue
            # skip if different bin
            if bnodes[nnode_bid].bin != cnode.bin:
                continue
            # we've found a suitable next node
            nbin_id_or = [nnode_bid, nnodeid_or[1]]
            break
        if debug_mode:
            print('\t\tnext: {}'.format(nbin_id_or), file=sys.stderr)
        if len(nbin_id_or) != 0:
            # if we've found a next node, extend the path
            if forward:
                path.append(nbin_id_or)
            else:
                # flip and add to the beginning of the path
                path.insert(0, [nbin_id_or[0], not nbin_id_or[1]])
            # mark that bin as "done"
            bnodes[nbin_id_or[0]].flag = True
            # get the Node object for the new current node
            cnode = bnodes[nbin_id_or[0]]
            # and traversal orientation
            corient_fwd = nbin_id_or[1]
            # increment the total coverage
            cov_total += cnode.getCoverageSum()
            # should we try to extend more? multiple cases when we should
            # we're extending forward and we're at the last bin of a node
            extend_more = corient_fwd and cnode.flank_end
            # we're extending backward and we're at the first bin of a node
            extend_more = extend_more or (not corient_fwd and cnode.flank_start)
        else:
            extend_more = False
    return (cov_total)


def writeGAF(path, bnodes):
    # prepare a name for that path
    cov_sum = 0
    path_len = 0
    path_string = []
    full_path_len = 0
    for bin_or in path:
        # get binned node object
        bin = bnodes[bin_or[0]]
        cov_sum += bin.getCoverageSum()
        path_len += bin.getLength()
        # full length from the full node
        full_path_len += bin.full_len
        # string representation of the path
        if bin_or[1]:
            path_string.append('>' + str(bin.id))
        else:
            path_string.append('<' + str(bin.id))
    # compute the mean coverage and make an id
    fake_mapq = min(round(float(cov_sum) / path_len), 254)
    cov_mean = round(float(cov_sum) / path_len, 1)
    gaf_v = '{}_{}_{}'.format(bin.id, bin.bin, cov_mean)
    # path length/start/end/strand
    gaf_v += '\t{}\t0\t{}\t+'.format(path_len, path_len)
    # path information: string representation and length
    gaf_v += '\t{}\t{}'.format(''.join(path_string),
                               full_path_len)
    # start at the first bin's offset
    # end at the length of the path + offset
    offset = bnodes[path[0][0]].offset
    gaf_v += '\t{}\t{}'.format(offset, path_len + offset)
    # residues matching, alignment block size, and mapping quality
    gaf_v += '\t{}\t{}\t{}'.format(path_len, path_len, fake_mapq)
    # cigar string
    gaf_v += '\tcs:Z::{}'.format(path_len)
    print(gaf_v)
    # return (True)


parser = argparse.ArgumentParser('Make a binned coverage track in GAF')
parser.add_argument('-g', help='pangenome graph (.pg, .xg, .vg)',
                    required=True)
parser.add_argument('-b', help='comma-sep list of breaks for coverage binning',
                    default='1,5,30')
parser.add_argument('-d', help='debug mode', action='store_true')
args = parser.parse_args()


# debug mode?
debug_mode = args.d

# load pangenome
pg = bdsg.bdsg.PackedGraph()
pg.deserialize(args.g)

# to record info on the current node
cur_node = ''
cur_coverage = []
# to bin nodes
cov_breaks = [int(i) for i in args.b.split(',')]
bnodes = {}
# prepare dict to access first/last bins of a node
first_bin = {}
last_bin = {}

# read input TSV stream
for line in fileinput.input(files='-'):
    line = line.rstrip().split('\t')
    # skip header
    if line[0] == 'seq.pos':
        continue
    # if new node, save current one
    if line[1] != cur_node:
        if cur_node != '':
            node = Node(cur_node, cov_arr=cur_coverage)
            node_bins = node.binCoverage(cov_breaks)
            for ii, bnode in enumerate(node_bins):
                bid = '{}_{}_{}'.format(bnode.id, bnode.bin, bnode.offset)
                bnodes[bid] = bnode
                if ii == 0:
                    first_bin[int(node.id)] = bid
            last_bin[int(node.id)] = bid
        cur_node = line[1]
        cur_coverage = [int(line[3])]
    else:
        cur_coverage.append(int(line[3]))
if len(cur_coverage) > 0:
    node = Node(cur_node, cov_arr=cur_coverage)
    node_bins = node.binCoverage(cov_breaks)
    for ii, bnode in enumerate(node_bins):
        bid = '{}_{}_{}'.format(bnode.id, bnode.bin, bnode.offset)
        bnodes[bid] = bnode
        if ii == 0:
            first_bin[int(node.id)] = bid
    last_bin[int(node.id)] = bid

print('{} binned nodes'.format(len(bnodes)), file=sys.stderr)

# enumerate some paths
npaths = 0
for sbin in bnodes.keys():
    # get next starting node that was not already put in a path
    if bnodes[sbin].flag:
        continue
    if debug_mode:
        print('starting node: ' + sbin, file=sys.stderr)
    # mark this node as done
    bnodes[sbin].flag = True
    # init a path made of pairs (node-bin id, is oriented fwd)
    path = [[sbin, True]]
    # to make sure there is some coverage
    cov_total = bnodes[sbin].getCoverageSum()
    # try to extend it to the forward direction
    cov_total += extendPath(path, bnodes, forward=True,
                            debug_mode=debug_mode)
    # try to extend it to the backward direction
    cov_total += extendPath(path, bnodes, forward=False,
                            debug_mode=debug_mode)
    # write the path if there is some coverage
    if cov_total > 0:
        npaths += 1
        writeGAF(path, bnodes)


print('{} paths created'.format(npaths), file=sys.stderr)


x = [1, 3]

def update(xx):
    xx += [5]
    xx.insert(0, 4)
    xx.append(6)
    return(True)

x
update(x)
x
