# Annotating known variants (SNPs/indels)

## GWAS catalog

Downloaded from the UCSC Genome Browser track:

```sh
wget https://hgdownload.soe.ucsc.edu/goldenPath/hg38/database/gwasCatalog.txt.gz
```

## Expression QTL from GTEx

Version 8 of GTEx eQTLs for each tissue

```sh
wget https://storage.googleapis.com/adult-gtex/bulk-qtl/v8/single-tissue-cis-qtl/GTEx_Analysis_v8_eQTL.tar

## to list the files in the TAR
tar --list -f GTEx_Analysis_v8_eQTL.tar
```

## HPRC pangenome 

We use the Minigraph-Cactus v1.1 pangenome. 
The script doesn't work on GBZ files directly, so we convert it first:

```sh
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.gbz
vg convert -t 4 -H -p hprc-v1.1-mc-grch38.gbz > hprc-v1.1-mc-grch38.pg
```

We also need to deconstruct the pangenome into a VCF file that will be used to match the known variants.

```sh
vg deconstruct -a -e -t 8 -P GRCh38 hprc-v1.1-mc-grch38.gbz | sed 's/GRCh38#0#//g' | gzip > hprc-v1.1-mc-grch38.vcf.gz
```

We are only annotating small variants (SNPs, indels) in this application (GWAS hits and eQTLs), so we also made a smaller VCF file with only the information we need.
It's 507Mb instead of 2.5Gb and is available at `TODO: add a public link to the VCF to make this (long) step optional`.
Use it if you want to reproduce this analysis or annotate other known SNPs/indels.

```sh
bcftools norm -m- hprc-v1.1-mc-grch38.vcf.gz | bcftools view -G -e "STRLEN(REF)>50 | MAX(STRLEN(ALT))>50" | bcftools annotate -x "INFO/AC,INFO/AF,INFO/AN,INFO/NS,INFO/LV,INFO/PS" | bcftools norm -m+ -o hprc-v1.1-mc-grch38.small.vcf.gz -O z
```

Note: this VCF matches the **GBZ** file of the Minigraph-Cactus v1.1 pangenome. 
The GFA file and VCF provided by the HPRC are slightly different and shouldn't be used.
The node IDs don't match exactly because some were split when making the GBZ (which handles nodes only up to 1024 bp).

## Match variants and make pangenome annotations

We used the `prepare_variant_paths.py` script like so

```sh
# for eQTLs
python3 prepare_variant_paths.py -p hprc-v1.1-mc-grch38.vcf.gz -g hprc-v1.1-mc-grch38.pg -v Spleen.v8.signif_variant_gene_pairs.txt.gz -s gtex_eqtls -l Spleen -o Spleen.GTEx_Analysis_v8_eQTL.hprc-v1.1-mc-grch38.gaf

# for the GWAS catalog
python3 prepare_variant_paths.py -p hprc-v1.1-mc-grch38.vcf.gz -g hprc-v1.1-mc-grch38.pg -v gwasCatalog.txt.gz -s gwas_catalog -o gwasCatalog.hprc-v1.1-mc-grch38.gaf
```

The output GAF can then be sorted with `vg gamsort`, compressed with `bgzip`, and indexed with `tabix`.
We prepared those GAFs for eQTLs in all tissues and the GWAS catalog using a Snakemake workflow:

```sh
snakemake --configfile config.yaml --cores 4 -p
```

Summaries about the annotation and resources used are available in the [`log`](log) and [`benchmark`](benchmark) directories.
A list of all the commands ran by the workflow is shown in `workflow.log`.

```sh
snakemake --configfile config.yaml -Fpn > workflow.log
```

A combined GAF with all variants was prepared with:

```sh
zcat *GTEx*sorted.gaf.gz gwasCatalog.hprc-v1.1-mc-grch38.sorted.gaf.gz | vg gamsort -G - | bgzip > gwas.eQTLs.gaf.gz
tabix -p gaf gwas.eQTLs.gaf.gz
```

## Variants from genotyping analysis

For this test, HG002 was genotyped using `vg call` from the aligned reads produced by the read sorting analysis ([`../readsorting`](../readsorting)).

```sh
snakemake --configfile config.yaml -pn genotype
```

A list of all the commands ran by the workflow for this analysis is shown in `workflow.genotype.log`.

```sh
snakemake --configfile config.yaml -Fpn genotype > workflow.genotype.log
```

Briefly, the VCF containing the genotype calls was converted to GAF using the `prepare_variant_paths_from_gt_vcf.py` script, sorted and indexed:

```sh
python3 prepare_variant_paths_from_gt_vcf.py -v HG002.gt.min30bp.vcf.gz -g hprc-v1.1-mc-grch38.pg -o HG002.gt.min30bp.gaf
vg gamsort -G HG002.gt.min30bp.gaf | bgzip > HG002.gt.min30bp.gaf.gz
tabix -p gaf HG002.gt.min30bp.gaf.gz
```
