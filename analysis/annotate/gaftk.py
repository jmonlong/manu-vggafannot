import argparse
import gzip
import logging


parser = argparse.ArgumentParser('Misc GAF tools')
parser.add_argument('-i', help='input GAF, potentially gzipped', required=True)
parser.add_argument('-gt', help='keep only this gene type', default='')
parser.add_argument('-st', help='strip transcript information from ID',
                    action='store_true')
parser.add_argument('-u', help='keep unique records (de-duplicate)',
                    action='store_true')
parser.add_argument('-c', help='combine samples', action='store_true')
parser.add_argument('-cs', help='max shfit to match record when combining samples',
                    type=int, default=2)
parser.add_argument('-mc', help='minimum coverage', type=float, default=-1)
parser.add_argument('-r', help='reference path as GAF', default='')
# this can be made with: vg paths -ARx hprc-v1.1-mc-grch38.gbz | gzip > hprc-v1.1-mc-grch38.ref.paths.gaf.gz
parser.add_argument('-mnr', help='minimum non-reference nodes', type=float, default=0.0)
args = parser.parse_args()

CACHE_SIZE = 1000
logger = logging.getLogger(__name__)

# position shifts to explore when combining samples
shift_bp = []
for bp in range(args.cs + 1):
    shift_bp += [bp, -1 * bp]

# open input GAF
if args.i.endswith('gz'):
    ingaf = gzip.open(args.i, 'rt')
else:
    ingaf = open(args.i, 'rt')


def prepareCombinedGAFrecord(rec, dedup_cache, sample_cache):
    new_gafr = dedup_cache[rec]
    # add sample names
    new_gafr[0] += ':{}haps'.format(len(sample_cache[rec]))
    # new GAF tag with haplotype names
    new_gafr.append('hn:Z:' + ','.join(sample_cache[rec]))
    return ('\t'.join(new_gafr))


def makeIDwithoutSample(rid, gafr, sep):
    # guess which type of ID we have based on the separator
    # for now ":" sep means a gene annotation, "#" means repeat masker
    if sep == ':':
        gaf_nosamp = [':'.join(rid[:2])] + gafr[1:]
        sample = rid[2]
    else:
        gaf_nosamp = [rid[0]] + gafr[1:]
        sample = '.'.join(rid[1:])
    gafid = '_'.join(gaf_nosamp)
    return ((gaf_nosamp, gafid, sample))


# to help deduplicate records
dedup_cache = {}
sample_cache = {}
cur_dedup_min_node = 0

# separator for the GAF record
# for now ":" sep we're dealing with a gene annotation, "#" means repeat masker
sep = ''
if args.mc > -1:
    logger.warning('ID separator guessed to be _')
    sep = '_'

# reference nodes
ref_nodes = {}
if args.r != '':
    logger.warning('Reading reference path from ' + args.r)
    # open reference gaf
    if args.i.endswith('gz'):
        inref = gzip.open(args.r, 'rt')
    else:
        inref = open(args.r, 'rt')
    for line in inref:
        line = line.split('\t')
        path = line[5].replace('<', '>').split('>')[1:]
        # save nodes in the dictionnary
        for node in path:
            ref_nodes[node] = line[0]
    inref.close()
    logger.warning('\t{} reference nodes extracted'.format(len(ref_nodes)))
else:
    if args.mnr > 0:
        logger.error('-r is needed when using -mnr')
        exit(1)

# read each record in the input GAF
for gafl in ingaf:
    gafr = gafl.rstrip().split('\t')

    # parse the record name if necessary
    rid = ''
    if args.gt != '' or args.st or args.c or args.mc:
        # guess separator based on first record
        if sep == '':
            if gafr[0].count(':') > gafr[0].count('#'):
                sep = ':'
            else:
                sep = '#'
            logger.warning('ID separator guessed to be ' + sep)
        rid = gafr[0].split(sep)

    # keep only one specific gene type
    if args.gt != '':
        # extract gene type from the record ID
        gene_type = rid[1]
        if len(rid) == 2:
            gene_type = 'transcript' if '_T' in rid[1] else 'gene'
        if gene_type != args.gt:
            continue

    # keep only coverage >= minimum coverage
    if args.mc > -1:
        cov = float(rid[3])
        if cov < args.mc:
            continue

    # get the minimum node ID if necessary
    if args.u or args.c or args.mnr > 0:
        path = gafr[5].replace('<', '>').split('>')[1:]
        min_node = min([int(node) for node in path])
        if args.mnr > 0:
            nr = []
            ref_path = ''
            for node in path:
                if node not in ref_nodes:
                    nr.append(str(node))
                else:
                    ref_path = ref_nodes[node]
            if float(len(nr)) / len(path) < args.mnr:
                continue
            else:
                gafr.append('nr:Z:' + ','.join(nr))
                gafr.append('nrp:f:{}'.format(round(float(len(nr)) /
                                                    len(path), 3)))
                if ref_path != '':
                    gafr.append('ref:Z:{}'.format(ref_path))
                else:
                    # look for a reference node
                    node = int(node)
                    attempt = 0
                    while str(node) not in ref_nodes and attempt < 1000:
                        node += 1
                        attempt += 1
                    if attempt < 1000:
                        gafr.append('ref:Z:{}'.format(ref_nodes[str(node)]))
                        gafr.append('refn:Z:{}'.format(node))

    # strip transcript information
    if args.st:
        if '_T' in rid[2]:
            rid[2] = rid[2].split('_T')[0]
            gafr[0] = ':'.join(rid[:3])

    new_gafr = '\t'.join(gafr)

    if args.u:
        if min_node != cur_dedup_min_node and len(dedup_cache) > CACHE_SIZE:
            # assuming the record are sorted by minimum node ID first
            # we are making sure to not miss upcoming duplicates
            # we can write the unique records for this chunk
            for rec in dedup_cache:
                print(rec)
            dedup_cache = {}
        # save the current record
        dedup_cache[new_gafr] = True
        cur_dedup_min_node = min_node
    elif args.c:
        if min_node != cur_dedup_min_node and len(dedup_cache) > CACHE_SIZE:
            # assuming the record are sorted by minimum node ID first
            # we are making sure to not miss upcoming duplicates
            # we can write the unique records for this chunk
            for rec in dedup_cache:
                print(prepareCombinedGAFrecord(rec, dedup_cache, sample_cache))
            dedup_cache = {}
            sample_cache = {}
        # save the current record in the cache
        # use a GAF ID that doesn't include the sample name
        gaf_nosamp, gafid, sample = makeIDwithoutSample(rid, gafr, sep)
        # annoying (bug?): look for record in the cache with up to
        # X bp difference in cols 7-8
        for shift in shift_bp:
            if gafid in sample_cache:
                # stop when we've matched the variant
                break
            # try shifting the position bp
            gafr_s = list(gafr)
            gafr_s[7] = str(int(gafr_s[7]) + shift)
            gafr_s[8] = str(int(gafr_s[8]) + shift)
            gaf_nosamp_s, gafid_s, s = makeIDwithoutSample(rid, gafr_s, sep)
            # if that ID has already been seen, use that one
            if gafid_s in sample_cache:
                gaf_nosamp = gaf_nosamp_s
                gafid = gafid_s
        # update caches
        dedup_cache[gafid] = gaf_nosamp
        if gafid not in sample_cache:
            sample_cache[gafid] = []
        sample_cache[gafid].append(sample)
        # update the current minimum node
        cur_dedup_min_node = min_node
    else:
        # print the record
        print(new_gafr)


# don't forget to finish a potentially ongoing dedup chunk
if args.u and len(dedup_cache) > 0:
    for rec in dedup_cache:
        print(rec)
if args.c and len(dedup_cache) > 0:
    for rec in dedup_cache:
        print(prepareCombinedGAFrecord(rec, dedup_cache, sample_cache))

ingaf.close()
