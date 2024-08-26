# Annotating the coverage of some of ENCODE's datasets

## ENCODE datasets

*Which datasets do we want to analyze?*

- ??
- Replicate with the most data (based on number of reads or file size?)

The data will be downloaded automatically using the URLs specified in [`sample_info.tsv`](sample_info.tsv) with `url_fq`.

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
