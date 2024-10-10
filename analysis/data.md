Data produced in this manuscript was deposited on Zenodo at: https://doi.org/10.5281/zenodo.13904205

BGZipped GAF files (`.gaf.gz`) and their index (`.gaf.gz.tbi`) are available.
They relate to three applications presented in the manuscript.

The same  HPRC draft pangenome v1 (GRCh38-based Minigraph-Cactus) was used for all analysis.
It's available in GBZ at `https://s3-us-west-2.amazonaws.com/human-pangenomics/pangenomes/freeze/freeze1/minigraph-cactus/hprc-v1.1-mc-grch38/hprc-v1.1-mc-grch38.gbz`

## HPRC annotations projected to the pangenome

The annotations for each haplotype used for the HPRC v1 pangenome were projected in graph space.
More information about the assemblies and annotations at https://github.com/human-pangenomics/HPP_Year1_Assemblies

- CAT gene annotations
    - `gene_CDS.gaf.gz` CDS regions only, for all haplotypes
    - `gene_exon.gaf.gz` exon regions only, for all haplotypes
- RepeatMasker annotation: `rm.gaf.gz`
- Tandem repeats from trf: `trf.gaf.gz`

## ATAC-seq coverage tracks for 7 ENCODE tissues

For each tissue, there is an indexed GAF file (`<tissue>.cov.gaf.gz`, `<tissue>.cov.gaf.gz.tbi`), a short table summary of the paths (`<tissue>.cov.sum.tsv`), and the number of paths in the GAF (`<tissue>.gaf.wc.txt`).
The seven tissues are:

- `breast_epithelium`
- `gastrocnemius_medialis`
- `gastroesophageal_sphincter`
- `PeyersPatch`
- `sigmoid_colon`
- `spleen`
- `thyroid_gland`

## Variants

Three types of genomic variants were projected to the pangenome:

- `eQTLs.gaf.gz` eQTLs from GTEx v8
- `gwasCatalog.hprc-v1.1-mc-grch38.sorted.gaf.gz` the GWAS Catalog
- `HG002.gt.min30bp.sorted.gaf.gz` structural variant calls from `vg call` (projected from the `HG002.gt.min30bp.vcf.gz` VCF).
