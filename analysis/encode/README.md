# Annotating the coverage of some of ENCODE's datasets

## ENCODE datasets

*Which datasets do we want to analyze?*

- ??
- Replicate with the most data (based on number of reads or file size?)

The data will be downloaded automatically using the URLs specified in [`sample_info.tsv`](sample_info.tsv) with `url_fq`.
If a sample is present multiple times in the TSV, the FASTQs will be concatenated before mapping to the pangenome.

## HPRC pangenome

We'll use the Minigraph-Cactus v1.1 HPRC pangenomes.

They were downloaded from:

```sh
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.gbz
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.dist
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.min
```

On Genotoul, they are currently at `/save/user/jmonlong/references`.

## Run the workflow on Genotoul

### Dependencies

#### Snakemake

Load the module `bioinfo/Snakemake/7.32.4`.

#### Singularity

Load the module `containers/singularity/3.9.9`.

The workflow will then use a prepared container with all the tools necessary (vg, tabix, python, etc).
The container is available at `quay.io/jmonlong/vg-work:1.59.0_v1` and the tools/versions are listed [here](https://github.com/jmonlong/docker-vg-work/tree/8b2792d934708d950b3077ba0b7aa3d64052dd1c).

#### HPRC pangenome on Genotoul

The indexes should be accessible from `/save/user/jmonlong/references`.

If not, download the files (see [HPRC pangenome](#hprc-pangenome)) and update the `config.yaml` file with their paths.

### Scripts, workflow and config

Copy the following files from this repo to Genotoul:

- `make_coverage_track.py` script which bins the read coverage.
- `Snakefile` which defines the workflow
- `config.yaml` with some general info, e.g. where the pangenome indexes are
- `sample_info.tsv` which define each sample and the URL of their FASTQs.

### Snakemake command

To check on a dry run:

```sh
module load containers/singularity/3.9.9 bioinfo/Snakemake/7.32.4
snakemake --configfile config.yaml -n
```

In practice, I run a long (but small) job that runs the *snakemake* command.
For example, `sbatch` a script like:

```sh
#!/bin/bash
#SBATCH -J run-smk
#SBATCH -o output_run-smk.out
#SBATCH -e error_run-smk.out
#SBATCH -t 336:00:00
#SBATCH -p unlimitq
#SBATCH --mem=4G

module load containers/singularity/3.9.9 bioinfo/Snakemake/7.32.4
snakemake --configfile config.yaml --jobs=20 -p --slurm --use-singularity --rerun-triggers mtime
```

One sample should take about ~3h.

## Figures/tables/examples

*Soon...*

```sh
Rscript ../sum-benchmark.R
```

|task                                    |    max_rss| mean_load|  cpu_time|h.m.s   |
|:---------------------------------------|----------:|---------:|---------:|:-------|
|index_gaf.thyroid_gland                 |       5.50|     77.48|      7.34|0:00:08 |
|index_gaf.gastrocnemius_medialis        |       5.39|     87.41|     10.66|0:00:12 |
|index_gaf.PeyersPatch                   |       5.16|     89.27|     14.92|0:00:16 |
|index_gaf.spleen                        |       5.48|     88.52|     14.93|0:00:16 |
|index_gaf.ENCSR917WJS                   |       5.38|     82.25|     15.18|0:00:18 |
|index_gaf.breast_epithelium             |       5.33|     76.41|     15.40|0:00:19 |
|index_gaf.sigmoid_colon                 |       5.51|     85.39|     15.45|0:00:17 |
|index_gaf.gastroesophageal_sphincter    |       5.34|     80.00|     15.59|0:00:19 |
|convert_gbz_to_pg                       |  13,807.30|     98.39|    288.94|0:04:53 |
|sort_cov_gaf.thyroid_gland              |     796.46|     98.70|    316.36|0:05:20 |
|sort_cov_gaf.gastrocnemius_medialis     |     795.61|    121.87|    364.00|0:04:58 |
|sort_cov_gaf.PeyersPatch                |     786.46|    127.81|    562.25|0:07:19 |
|sort_cov_gaf.ENCSR917WJS                |     928.39|    123.75|    592.31|0:07:58 |
|sort_cov_gaf.gastroesophageal_sphincter |     784.54|    128.77|    641.70|0:08:18 |
|sort_cov_gaf.spleen                     |     788.66|     97.88|    672.72|0:11:27 |
|sort_cov_gaf.breast_epithelium          |     908.63|    126.08|    677.42|0:08:57 |
|sort_cov_gaf.sigmoid_colon              |     788.58|     96.08|    702.63|0:12:11 |
|make_cov.thyroid_gland                  |  95,876.23|    155.59|  8,147.74|1:27:16 |
|make_cov.gastrocnemius_medialis         | 101,974.03|    151.26|  8,533.76|1:34:01 |
|make_cov.PeyersPatch                    | 106,859.24|    131.04|  9,360.04|1:59:02 |
|make_cov.sigmoid_colon                  | 106,863.62|    143.71|  9,673.90|1:52:11 |
|make_cov.gastroesophageal_sphincter     | 109,562.08|    153.77|  9,808.20|1:46:18 |
|make_cov.spleen                         | 107,509.87|    151.83| 10,251.81|1:52:31 |
|make_cov.ENCSR917WJS                    | 109,521.16|    174.57| 10,800.08|1:43:06 |
|make_cov.breast_epithelium              | 111,059.25|    156.97| 11,080.25|1:57:38 |
|map_reads.thyroid_gland                 |  55,569.54|    725.23| 16,428.36|0:37:45 |
|map_reads.gastrocnemius_medialis        |  55,692.81|    700.66| 17,257.11|0:41:02 |
|map_reads.gastroesophageal_sphincter    |  55,712.97|    763.49| 26,240.65|0:57:16 |
|map_reads.spleen                        |  55,714.13|    735.76| 27,279.73|1:01:47 |
|map_reads.PeyersPatch                   |  55,761.16|    717.50| 28,686.33|1:06:38 |
|map_reads.sigmoid_colon                 |  55,612.79|    765.08| 29,517.25|1:04:18 |
|map_reads.breast_epithelium             |  55,581.25|    754.67| 32,088.55|1:10:51 |
|map_reads.ENCSR917WJS                   |  55,786.93|    765.53| 57,482.93|2:05:08 |
