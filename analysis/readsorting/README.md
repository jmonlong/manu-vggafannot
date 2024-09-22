## Short sequencing reads from HG002

30x HiSeq reads downloaded from the HPRC repository:

```sh
wget -O HG002_HiSeq30x_subsampled_R1.fastq.gz -nv https://s3-us-west-2.amazonaws.com/human-pangenomics/NHGRI_UCSC_panel/HG002/hpp_HG002_NA24385_son_v1/ILMN/downsampled/HG002_HiSeq30x_subsampled_R1.fastq.gz
wget -O HG002_HiSeq30x_subsampled_R2.fastq.gz -nv https://s3-us-west-2.amazonaws.com/human-pangenomics/NHGRI_UCSC_panel/HG002/hpp_HG002_NA24385_son_v1/ILMN/downsampled/HG002_HiSeq30x_subsampled_R2.fastq.gz
```

## HPRC pangenome

We'll use the Minigraph-Cactus v1.1 HPRC pangenomes.

They were downloaded from:

```sh
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.gbz
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.hapl
```

## Map, sort and index reads in GAM and GAF

```sh
snakemake --configfile config.yaml -n
```

## Results

```sh
> tree -h results/
results/
├── [ 2.4G]  sample_pg.HG002.gbz
├── [ 4.0K]  sorted
│   ├── [  52G]  HG002.gaf.gz
│   ├── [ 132K]  HG002.gaf.gz.tbi
│   ├── [ 108G]  HG002.gam
│   └── [ 9.4M]  HG002.gam.gai
└── [ 4.0K]  unsorted
    ├── [  55G]  HG002.gaf.gz
    └── [ 137G]  HG002.gam
> zcat results/unsorted/HG002.gaf.gz | wc -l
681708020   
```

Resources used (from running `Rscript ../sum-benchmark.R`):


|task                          |   max_rss| mean_load|   cpu_time|h.m.s    |
|:-----------------------------|---------:|---------:|----------:|:--------|
|HG002.index_distance          | 54,274.38|     94.09|     695.83|0:12:19  |
|HG002.index_gaf               |      5.42|     93.83|   1,045.14|0:18:33  |
|HG002.sample_haplotypes       | 29,072.87|    344.24|   1,171.32|0:05:40  |
|HG002.index_minimizer         | 45,915.90|    567.39|   1,269.08|0:03:43  |
|HG002.count_kmer_in_reads     | 61,153.05|    566.00|   4,691.35|0:13:48  |
|HG002.sort_gaf                |  1,904.83|     98.92|  23,294.76|6:32:28  |
|HG002.sort_gam                |  6,236.60|     98.84|  41,928.87|11:46:58 |
|HG002.gam_to_gaf              |  8,648.95|    395.71|  43,333.25|3:02:30  |
|HG002.map_short_reads_giraffe | 47,329.29|  1,572.82| 149,669.25|2:38:35  |


## Query time

1. Prepare 10,000 node interval of length 50 (nodes) in the reference path (see [sample-nodes.py](sample-nodes.py)).
2. Extract the reads for each of these slices and time it (approximately).

```sh
vg paths -x ~/Documents/genomedata/hprc-v1.1-mc-grch38.gbz -A -Q GRCh38 | python3 sample-nodes.py > random-node-intervals.txt

rm -f slice.gaf
date
# 18:07:14
for nodeint in `cat random-node-intervals.txt`
do
    tabix results/sorted/HG002.gaf.gz $nodeint >> slice.gaf
done
date
# 18:18:11

wc -l slice.gaf
# 17068487 slice.gaf
```
