## Tabix-based index files

Three files are used, each one indexed with tabix (additional `.tbi` file):

1. `nodes.tsv.gz` contains the sequence of each node.
2. `pos.bed.gz` contains the position (as node intervals) of regions on each haplotype.
3. `haps.gaf.gz` contains the path followed by each haplotype (split in pieces).

Briefly, these three index files can be quickly queried to extract a subgraph covering a region of interest: the `pos.bed.gz` index can first tell us which nodes are covered, then the `nodes.tsv.gz` index gives us the sequence of these nodes, and finally we can stitch the haplotype pieces in those nodes from the `haps.gaf.gz` index.
This approach was implemented in a `chunkix.py` script which can produce a GFA file or files used by the sequenceTubeMap. 
The sequenceTubeMap uses this script internally when given tabix-based index files.

## Creating the index files

The `pgtabix.py` script was used to produce the new tabix-based index files.
However, it takes a GFA file (possibly gzipped) as input.
In some cases, you will want to use exactly the same pangenome space as a specific GBZ file. 
For example, to visualize reads or annotation on that pangenome. 
The GFA provided in the HPRC repo might not match exactly because some nodes may have been split when making the GBZ file. 
Hence, the [HPRC Minigraph-Cactus v1.1 GBZ](https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.gbz) was first converted to GFA (without translating the nodes back to the original GFA) with:

```sh
vg convert --no-translation -f -t 4 hprc-v1.1-mc-grch38.gbz | gzip >  hprc-v1.1-mc-grch38.gfa.gz
```

This gzipped GFA file was then given to the `pgtabix.py` script to make the tabix-indexed files.

```sh
python3 pgtabix.py -g hprc-v1.1-mc-grch38.gfa.gz -o hprc-v1.1-mc-grch38
```

It takes about 1h30-2h to build index files for the Minigraph-Cactus v1.1 pangenome.

Those index files will be made available soon (*ZENODO??*).

## Benchmarking query speed

The `chunkix.py` script and `vg chunk` were timed on random regions of different sizes using the `query.time.test.py` script.
This assumes that the tabix-indexed files are present (for `chunkix.py`) and the GBZ file (for `vg chunk`).

It also assumes that a file called `contig.lengths.txt` and containing the name and length of every contig in the pangenome is present.
It is used to select a random query covering any haplotype. 
Although it's included in this repo, it was made with:

```sh
vg paths -E -x hprc-v1.1-mc-grch38.gbz > contig.lengths.txt
```

We tested three different region size (`-s` below):

```sh
python3 query.time.test.py -r -n 50 -s 100 > benchmark.query.50.100.tsv
python3 query.time.test.py -r -n 50 -s 1000 > benchmark.query.50.1000.tsv
python3 query.time.test.py -r -n 50 -s 10000 > benchmark.query.50.10000.tsv
```

A summary of the query time is compiled in [this R-markdown report](query.time.test.md).

## Using tabix-based index files in the sequenceTubeMap

The version on the `tabix` branch can use those index files, for example when mounted files are provided:

- the `pos.bed.gz` index in the *graph* field
- the `nodes.tsv.gz` index in the *node* field
- the `haps.gaf.gz` index in the *haplotype* field

![](mount.tabix.index.png)

Once the index files are mounted, one can query any region on any haplotype in the form *HAPNAME_CONTIG:START-END*.

Other tracks, for example reads or annotations in bgzipped/indexed GAF files, can be added as *reads* in the menu.

![](mount.tabix.index.annot.png)

Of note, you can set a color for each track using the existing palettes or by picking a specific color.

![](mount.tabix.index.annot.color.png)

A docker container with this new sequenceTubeMap version, and all the dependencies necessary, is available at `quay.io/jmonlong/sequencetubemap:tabix_dev`.

To use it, run:

```sh
docker run -it -p 3210:3000 -v `pwd`:/data quay.io/jmonlong/sequencetubemap:tabix_dev
```

Of note, the `-p` option redirects port 3000 to 3210. 
In practice, pick an unused port.

Then open: http://localhost:3210/

Note: This assumes all files (pangenomes, reads, annotations) are in the current working directory or in subdirectories.
