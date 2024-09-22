# Projecting annotations from genomes to pangenome

## Annotation data

For this experiment, we worked with annotations produced for each assembled haplotype of the HPRC freeze 1.
These are the haplotypes present in the pangenome (see below).
An index of the paths for each annotation file is available at [https://github.com/human-pangenomics/HPP_Year1_Assemblies/tree/main/annotation_index](https://github.com/human-pangenomics/HPP_Year1_Assemblies/tree/main/annotation_index).

We ran the pipeline on:

- BED files annotating segmental duplications, tandem repeats, and RepeatMasker-annotated repeats
- GFF3 files for the gene annotation (from CAT)

```sh
wget https://raw.githubusercontent.com/human-pangenomics/HPP_Year1_Assemblies/main/annotation_index/Year1_assemblies_v2_genbank_Seg_Dups.index
wget https://raw.githubusercontent.com/human-pangenomics/HPP_Year1_Assemblies/main/annotation_index/Year1_assemblies_v2_genbank_TRF.index
wget https://raw.githubusercontent.com/human-pangenomics/HPP_Year1_Assemblies/main/annotation_index/Year1_assemblies_v2_genbank_Repeat_Masker.index
wget https://raw.githubusercontent.com/human-pangenomics/HPP_Year1_Assemblies/main/annotation_index/Year1_assemblies_v2_genbank_CAT_genes.index
```

### Pangenome

We used the GRCh38-based Minigraph-Cactus pangenome v1.1.

They were downloaded from:

```sh
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.gbz
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.dist
wget https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.min
```

## Workflow

A workflow was implemented in Snakemake to annotate the different annotations on all the haplotypes. 
Under the hood, the workflow:

1. prepares the pangenomes
2. pre-processes the annotation files
3. projects the annotation onto the pangenome (`vg annotate`)
4. sorts and indexes the pangenomic annotations (`vg gamsort`)

For example, assuming the full pangenome GBZ file and raw annotations are locally available, the commands might look like:

```sh 
## add the haplotype as a refernece path in the GBZ
vg gbwt -Z --set-tag "reference_samples=HG00438" --gbz-format -g gbz/HG00438.hprc-v1.1-mc-grch38.gbz hprc-v1.1-mc-grch38.gbz
## pre-process annotation
python3 pre-vg-annotate.py -i raw_annotation/HG00438.1.grch38.gff3.gz --add-prefix HG00438#1# --use-name-id | gzip > prep_annotation/gene_HG00438.1.gff3.gz
## project annotation onto pangenome
gunzip -c prep_annotation/gene_HG00438.1.gff3.gz | vg annotate -x gbz/HG00438.hprc-v1.1-mc-grch38.gbz -f - | vg convert -G - gbz/HG00438.hprc-v1.1-mc-grch38.gbz | gzip > unsorted_gaf/gene_HG00438.1.gaf.gz
## sort GAF
vg gamsort -t 1 -pG unsorted_gaf/gene_HG00438.1.gaf.gz | bgzip > gaf/gene_HG00438.1.gaf.gz
## index GAF
tabix -p gaf gaf/gene_HG00438.1.gaf.gz
```

To run the workflow:

```sh
snakemake -p --use-singularity
```

### Pre-processing of the annotation files

Ideally, we would record relevant metadata in the GAF file. 
For example, haplotype of origin, element name and additional information (e.g. gene type, annotation type, repeat class).
In practice, the current implementation of `vg annotate` only saves one read/path/annotation "name" per annotation. 
The most relevant information was then crammed into this "name" by modifying the raw annotation files before projection to the pangenome.
The annotation files were modified using the ([`pre-vg-annotate.py`](pre-vg-annotate.py)) python script to:

- Rename the elements so that it includes the haplotype of origin. This will later help differentiating the same genes/repeats/etc from different haplotypes.
- Create more descriptive names (for repeats).
- Add a prefix to the contig names to match the haplotype names in the pangenome (usually adding `{SAMPLE}#{HAP}#`), if needed.

#### Pre-process gene annotation from CAT

```sh
python3 pre-vg-annotate.py -i {input} --add-prefix {pref} --use-name-id | gzip > {output}
```

where:

- `{pref}` is the haplotype name prefix (e.g. `HG00438#1#`) to add to the contig names.
- `--use-name-id` to replace the *Name* value with the value of *Name* and *ID*, seprated by a `:`. For example, the CAT annotations have `ID=HG00438.1_G0000001;Name=WASHC1` which will be changed to `ID=HG00438.1_G0000001;Name=WASHC1:HG00438.1_G0000001`. 

#### Pre-process tandem repeats from TRF

```sh
python3 pre-vg-annotate.py -i {input} --add-suffix "{suff}" --add-rep-n | gzip > {output}
```

where: 

- `{suff}` is the haplotype name suffix (e.g. `#HG00438#1`) to add to the repeat name.
- `--add-rep-n` to format the repeat names as `(<MOTIF>)<N>`

#### Pre-process segmental duplications

```sh
python3 pre-vg-annotate.py -i {input} --add-suffix "{suff}" --add-len-fracm | gzip > {output}
```

where: 

- `{suff}` is the haplotype name suffix (e.g. `#HG00438#1`) to add to the SD name.
- `--add-len-fracm` to name the SD as `<LENGTH>bp_<FRACMATCH>`

#### Pre-process RepeatMasker annotation

```sh
python3 pre-vg-annotate.py -i {input} --add-suffix "{suff}" --add-rm-class | gzip > {output}
```

where: 

- `{suff}` is the haplotype name suffix (e.g. `#HG00438#1`) to add to the SD name.
- `--add-rm-class` to prefix the repeat name with its class

### Simplify and combine annotations

```sh
python3 gaftk.py -i gene_HG02080.2.gaf.gz -gt CDS -st -u | bgzip > gene_HG02080.2.CDS.gaf.gz
python3 gaftk.py -i gene_HG01978.2.gaf.gz -gt CDS -st -u | bgzip > gene_HG01978.2.CDS.gaf.gz

zcat gene_HG02080.2.CDS.gaf.gz gene_HG01978.2.CDS.gaf.gz | vg gamsort -G - | bgzip > gene_HG02080.2.HG01978.2.CDS.gaf.gz

python3 gaftk.py -i gene_HG02080.2.HG01978.2.CDS.gaf.gz -c | vg gamsort -G - | bgzip > gene_HG02080.2.HG01978.2.CDS.c.gaf.gz

```
