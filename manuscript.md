---
title: Current options to index, represent, and visualize annotations in a pangenome with the vg toolkit
keywords:
- pangenome
- annotation
- alignment
lang: en-US
date-meta: '2024-10-02'
author-meta:
- Adam M. Novak
- Dickson Chung
- Glenn Hickey
- Sarah Djebali
- Toshiyuki T. Yokoyama
- Erik Garrison
- Benedict Paten
- Jean Monlong
header-includes: |
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta property="og:type" content="article" />
  <meta name="dc.title" content="Current options to index, represent, and visualize annotations in a pangenome with the vg toolkit" />
  <meta name="citation_title" content="Current options to index, represent, and visualize annotations in a pangenome with the vg toolkit" />
  <meta property="og:title" content="Current options to index, represent, and visualize annotations in a pangenome with the vg toolkit" />
  <meta property="twitter:title" content="Current options to index, represent, and visualize annotations in a pangenome with the vg toolkit" />
  <meta name="dc.date" content="2024-10-02" />
  <meta name="citation_publication_date" content="2024-10-02" />
  <meta property="article:published_time" content="2024-10-02" />
  <meta name="dc.modified" content="2024-10-02T15:15:09+00:00" />
  <meta property="article:modified_time" content="2024-10-02T15:15:09+00:00" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Adam M. Novak" />
  <meta name="citation_author_institution" content="UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA" />
  <meta name="citation_author_orcid" content="0000-0001-5828-047X" />
  <meta name="citation_author" content="Dickson Chung" />
  <meta name="citation_author_institution" content="UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA" />
  <meta name="citation_author" content="Glenn Hickey" />
  <meta name="citation_author_institution" content="UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA" />
  <meta name="citation_author" content="Sarah Djebali" />
  <meta name="citation_author_institution" content="IRSD - Digestive Health Research Institute, University of Toulouse, INSERM, INRAE, ENVT, UPS, Toulouse, France" />
  <meta name="citation_author_orcid" content="0000-0002-0599-1267" />
  <meta name="citation_author" content="Toshiyuki T. Yokoyama" />
  <meta name="citation_author_institution" content="Department of Computational Biology and Medical Sciences, Graduate School of Frontier Sciences, The University of Tokyo, Chiba, Japan" />
  <meta name="citation_author" content="Erik Garrison" />
  <meta name="citation_author_institution" content="Department of Genetics, Genomics and Informatics, University of Tennessee Health Science Center, Memphis, TN, USA" />
  <meta name="citation_author_orcid" content="0000-0003-3821-631X" />
  <meta name="citation_author" content="Benedict Paten" />
  <meta name="citation_author_institution" content="UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA" />
  <meta name="citation_author_orcid" content="0000-0001-8863-3539" />
  <meta name="citation_author" content="Jean Monlong" />
  <meta name="citation_author_institution" content="IRSD - Digestive Health Research Institute, University of Toulouse, INSERM, INRAE, ENVT, UPS, Toulouse, France" />
  <meta name="citation_author_orcid" content="0000-0002-9737-5516" />
  <link rel="canonical" href="https://jmonlong.github.io/manu-vggafannot/" />
  <meta property="og:url" content="https://jmonlong.github.io/manu-vggafannot/" />
  <meta property="twitter:url" content="https://jmonlong.github.io/manu-vggafannot/" />
  <meta name="citation_fulltext_html_url" content="https://jmonlong.github.io/manu-vggafannot/" />
  <meta name="citation_pdf_url" content="https://jmonlong.github.io/manu-vggafannot/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://jmonlong.github.io/manu-vggafannot/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://jmonlong.github.io/manu-vggafannot/v/59ab9710a519d9d1005c6fd46dd0c7ac757fe743/" />
  <meta name="manubot_html_url_versioned" content="https://jmonlong.github.io/manu-vggafannot/v/59ab9710a519d9d1005c6fd46dd0c7ac757fe743/" />
  <meta name="manubot_pdf_url_versioned" content="https://jmonlong.github.io/manu-vggafannot/v/59ab9710a519d9d1005c6fd46dd0c7ac757fe743/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography:
- content/manual-references.json
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...






<small><em>
This manuscript
([permalink](https://jmonlong.github.io/manu-vggafannot/v/59ab9710a519d9d1005c6fd46dd0c7ac757fe743/))
was automatically generated
from [jmonlong/manu-vggafannot@59ab971](https://github.com/jmonlong/manu-vggafannot/tree/59ab9710a519d9d1005c6fd46dd0c7ac757fe743)
on October 2, 2024.
</em></small>



## Authors



+ **Adam M. Novak**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-5828-047X](https://orcid.org/0000-0001-5828-047X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [adamnovak](https://github.com/adamnovak)
    <br>
  <small>
     UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA
  </small>

+ **Dickson Chung**
  <br>
  <small>
     UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA
  </small>

+ **Glenn Hickey**
  <br>
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [glennhickey](https://github.com/glennhickey)
    <br>
  <small>
     UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA
  </small>

+ **Sarah Djebali**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-0599-1267](https://orcid.org/0000-0002-0599-1267)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [sdjebali](https://github.com/sdjebali)
    <br>
  <small>
     IRSD - Digestive Health Research Institute, University of Toulouse, INSERM, INRAE, ENVT, UPS, Toulouse, France
  </small>

+ **Toshiyuki T. Yokoyama**
  <br>
  <small>
     Department of Computational Biology and Medical Sciences, Graduate School of Frontier Sciences, The University of Tokyo, Chiba, Japan
  </small>

+ **Erik Garrison**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0003-3821-631X](https://orcid.org/0000-0003-3821-631X)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [ekg](https://github.com/ekg)
    <br>
  <small>
     Department of Genetics, Genomics and Informatics, University of Tennessee Health Science Center, Memphis, TN, USA
  </small>

+ **Benedict Paten**
  <br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0001-8863-3539](https://orcid.org/0000-0001-8863-3539)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [benedictpaten](https://github.com/benedictpaten)
    <br>
  <small>
     UC Santa Cruz Genomics Institute, University of California, Santa Cruz, Santa Cruz, CA, USA
  </small>

+ **Jean Monlong**
  ^[✉](#correspondence)^<br>
    ![ORCID icon](images/orcid.svg){.inline_icon width=16 height=16}
    [0000-0002-9737-5516](https://orcid.org/0000-0002-9737-5516)
    · ![GitHub icon](images/github.svg){.inline_icon width=16 height=16}
    [jmonlong](https://github.com/jmonlong)
    <br>
  <small>
     IRSD - Digestive Health Research Institute, University of Toulouse, INSERM, INRAE, ENVT, UPS, Toulouse, France
  </small>


::: {#correspondence}
✉ — Correspondence possible via email to
Jean Monlong \<jean.monlong@inserm.fr\>.


:::


## Abstract {.page_break_before}

The current reference genome is the backbone of diverse and rich annotations. 
Simple text formats, like VCF or BED, have been widely adopted and helped the critical exchange of genomic information. 
To enable similar enrichment for a pangenome reference, there is a dire need for tools and formats enabling pangenomic annotation. 
The Graph Alignment Format (GAF) is a text format, tab-delimitted like BED/VCF files, which was proposed to represent alignments.
While it could be used to represent any type of annotation in a pangenome graph, there is no tools to index and query them efficiently.

Here, we present extension to vg and HTSlib that provide efficient sorting, indexing and querying for GAF files.
With this approach, annotations overlapping a subgraph can be extracted quickly.
Paths are sorted based on the IDs of traversed nodes, compressed with BGZIP, and indexed with HTSlib/tabix that we extended to work with the GAF format. 
Compared to the GAM format, GAF files are easier to write text files and we show that they are twice as fast to sort and twice as small on disk.
In addition, we updated `vg annotate` to better produce graph annotations, as paths, starting from annotation files relative to linear references. 
More precisely, it can to take annotations in BED or GFF3 files, written relative to reference paths or haplotypes, and produce GAF files representing their paths through the pangenome.

We showcased these new commands on several applications. 
We projected annotations for all haplotypes in the latest draft human pangenome (HPRC v1.1 GRCh38-based Minigraph-Cactus pangenome), including genes, segmental duplications, tandem repeats and repeats annotations. 
We also projected known variants from the GWAS catalog and expression QTLs from the GTEx project to the pangenome. 
Finally, we reanalyzed ATAC-seq data from ENCODE to highlight how a coverage track could look like in a pangenome graph.
In all cases, these rich annotations can be quickly queried with `vg` and visualized using existing tools like the sequenceTubeMap or Bandage.




<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css">

## Introduction

<!-- Non-exhaustive tool list at https://pangenome.github.io/ -->

The current reference genome is the backbone of diverse and rich annotations. 
It is used as a reference to map sequencing reads.
The coordinate system that it provides is used by large annotation databases gathering functional elements, known variant information, genomic elements. 
Over the past decades, the organization and visualization of these annotations has been central for understanding and sharing results from genomic studies.
In practice, annotations are typically saved in additional files following a text format that can be compressed and indexed for fast query (e.g. VCF, BED, GFF).
Under the hood, the HTSlib library supports the indexing of the most used file formats[@htslib].
These annotation files are easy to write and to load in software like IGV[@igv] or website like the UCSC Genome Browser[@doi:10.1093/nar/gkac1072].

With the improved genome sequencing technologies, more high-quality genomes can be produced and combined into pangenomes.
A pangenome represents multiple genomes, often as a graph describing adjancency (edges) of the sequences (nodes) in the genomes.
Tools to work with such pangenomes are still in their infancy although there are now several options that shows improved performance over traditional approaches.
In particular, sequencing data analysis benefits from using pangenomes as a reference for read mapping[@vg;@giraffe], variant calling[@vgsv], peak calling[@doi:10.1371/journal.pcbi.1006731;@doi:10.1186/s13059-020-02038-8], or transcript expression quantification[@doi:10.1038/s41592-022-01731-9].
This means that we are now manipulating genomic objects like sequencing reads, epigenetic regions, genomic variants, in the pangenome graph space.
Currently, those results are typically projected to the linear reference genome.
As for linear genome reference, it will be essential to be able to organize and visualize genomic annotation in the pangenome.
A lack of user-friendly querying and visualization options would hamper the adoption of the pangenomic paradigm.

Several interactive visualization tools for pangenomes already exist but mostly focus on representing the graph topology with specialized integration of additional information layers. 
Bandage is an interactive assembly graph visualization tool which can scale to pangenomes up to hundreds of thousands of nodes on modern computers[@bandage].
GfaViz is another interactive sequence graph visualization tool which supports the GFA 2 format and its new features[@doi:10.1093/bioinformatics/bty1046].
In particular, it can represent the different paths annotated in the GFA file.
GfaViz cannot load additional annotation files: the annotations, written for example as GFA *paths*, must be included in the main pangenome file to be accessible during exploration. 
<!-- [`gfaestus`](https://github.com/chfi/gfaestus)???. -->
The sequenceTubeMap visualizes the pangenome and sequencing reads aligned to it, allowing the user to query specific regions[@tubemap].
MoMI-G, or Modular Multi-scale Integrated Genome Graph Browser, focuses on the visualization of structural variants[@doi:10.1186/s12859-019-3145-2].
Variants are interactively selected and represented in a pangenome view a custom sequenceTubeMap representation. 
Supporting reads and genome annotations can also be included in that representation. 
Currently, only the reference genome path can be annotated from files in BED/GFF/WIG format.
Panache is another pangenomic tool specializing in gene-centric visualization of a linearized view of the pangenome, where blocks of homologous sequences are represented side by side[@doi:10.1093/bioinformatics/btab688].
The blocks are interactively explored in a web-based application to explore their gene content and their absence/presence in the different genimes.
Panache is notably used in the Banana Genome Hub[@doi:10.1093/database/bat035].
In summary, some visualization tools exist but it is not yet clear how to best provide additional annotation layers to their graph representation.

A few options also exist to display static representations of a pangenome graph (or subgraph).
The `vg` toolkit can output a pangenome and alignments in the DOT format. 
Paths can be displayed too, although the image can become hard to read when many paths are included or in large grahs.
The `odgi` toolkit offers visualizations that scale better to larger graphs and annotations[@odgi]. 
The pangenome is, for example, linearized using an 1D layout[@layout] and annotations displayed on top of the graph as an array/heatmap.
Of note, `odgi` implemented two options to add annotations from external BED files: one to convert annotations to a CSV file to help color nodes in Bandage, another by injecting new paths into a graph before visualization.
One limitation to injecting new paths into a pangenome is that paths must then start at the beginning of a node as we cannot provide an *offset* value to specify the base at which a path must start.

There is a dire need for a format supporting annotations in the pangenome and that can is easy to create, index and query.
As demonstrated by the success of the BED, GFF or VCF formats, it could help the critical exchange of (pan)genomic information, and allow pangenomic tools access additional information in the pangenomic space.
The Graph Alignment Format (GAF) text format, which was proposed to represent alignments, could be used to represent any type of annotation in a pangenome graph.
It's the lack of techniques to compress, index and query it that limits its adoption at a larger scale.
Here, we present new features of the `vg` and HTSlib ecosystem that provide efficient indexing and querying for pangenomic annotations represented as paths in the GAF format.
We illustrate its values in several applications: projecting and visualizing gene and repeat annotations, summarizing open-chromatin from epigenomics sequencing datasets, or positioning known variants in the pangenome.


## Methods

### Indexing paths in GAF files

The sorting and indexing algorithm is most efficient and makes sense when node IDs are integer sorted based on the topology of the pangenome graph.
This is the case for pangenomes constructed by minigraph-cactus[@minigraph_cactus], PGGB[@pggb], or `vg construct`[@vg].
Otherwise, the pangenome graph can be *sorted*, i.e. changing the node IDs, using `vg` or `odgi`[@odgi].
If the node IDs are sorted integers, a short path through the graph should only traverse nodes with IDs contained in a small interval (see Fig @fig:index).
The main approach of the GAF sorting and indexing approach is to work with those intervals.
Hence, to sort a GAF file, each path is first parsed to extract the minimum and maximum node IDs.
The paths are then sorted first by their minimum ID, and then by their maximum ID. 
This is similar to the approach used to sort BED or VCF files on linear genomes: they are sorted by sequence name, then start position, then end position.

![
**Path sorting and indexing using vg and HTSlib/tabix**
**A.** A region of pangenome is represented with nodes (containing sequences) in yellow and edges in black. 
The node IDs are topologically sorted integers, ranging here from 23 to 36.
Three paths are highlighted in red, blue and green. 
**B.** The three paths are written with the GAF syntax, by specifying the orientations (`<`/`>`) and IDs of the traversed nodes.
For each path, the node range *n-N*, between the minimum and maximum node IDs, is used for sorting the path.
**C.** Overview of the workflow to sort a GAF file using `vg gamsort`, compress it with `bgzip` and index using `tabix`. 
**D.** The small *.tbi* index file helps query slices of the GAF file quickly. For example using `tabix`, or `vg` subcommands like `find` or `chunk`.
](figures/gafindexing.png "GAF indexing"){#fig:index}

A GAF sorting feature has been added to the `vg` toolkit, within the `gamsort` subcommand.
It first sorts chunks of GAF records (e.g. reads), to avoid having to hold the entire set in memory.
The sorted chunks are then merged into the final sorted GAF file.
This GAF sorting implementation was included in `vg` in version 1.56.
A sorted GAF file can be compressed in the BGZF format using `bgzip`.
The BGZF format is an implementation of the standard gzip format that compresses a file by block to facilitate their random access.
It is used to compress among others, VCF, BED, or BAM files with HTSlib[@htslib].

HTSlib[@htslib] was then modified to index bgzipped GAF files.
Similar to other tab-separated file like VCF or BED, a *gaf* preset was added to `tabix`.
For BED or VCF, `tabix` extract the interval information from the columns with the sequence names and genomic position[@tabix]. 
In the new *gaf* preset, it instead parses the path information in the GAF file to extract the minimum and maximum node IDs.
The indexing is then based on this interval, the same as used for the sorting described above.

We tested the GAF sorting and indexing performance on 30X coverage Illumina short reads from HG002.
The reads were downloaded from `https://s3-us-west-2.amazonaws.com/human-pangenomics/NHGRI_UCSC_panel/HG002/hpp_HG002_NA24385_son_v1/ILMN/downsampled/`.
We mapped them using giraffe[@giraffe] on a personnalized pangenome[@hapsamp] from the HPRC v1.1 Minigraph-Cactus pangenome.
The reads were outputted in GAM first to compare the file size and sorting runtimes.
The GAM file was sorted with `vg gamsort`.
It was then converted to a GAF file using `vg convert` and sorted using `vg gamsort` with the new GAF sorting mode described above.
We compared the file sizes and sorting runtimes between both approach.
The query time was also measured on ten thousand regions of the pangenome defined as node ranges. 
Those node ranges were defined by picking a random starting node position the reference path and walking 50 steps along that path.
The commands and details for this benchmarking is available in the `analysis/readsorting` folder of this paper's repository[@repo].

### Querying GAF files

Instead of indexing on a sequence name and genomic position, we can query on a node interval.
In HTSlib, `tabix` was modified to disregard the sequence name when querying intervals for a GAF file. 
The interval is defined by the values typically used for the *start* and *end* position of genomic coordinates.

Commands to query slices of the pangenome in `vg` were also updated.
The `find` and `chunk` subcommands use the updated HTSlib library to extract the appropriate paths from the nodes selected.
Internally, those commands identify a first subgraph, for example corresponding to a genomic interval on the reference path provided by the user. 
This subgraph is then extended with more *context* to include non-reference regions of the graph.
The amount of context is also controlled by the user.
Finally, the subgraph or the paths (usually reads) overlapping these nodes are extracted.
This last step was updated to be able to extract paths in an indexed GAF file using HTSlib.
As for sorted GAM files, it is now possible to extract a slice of a indexed GAF file based on node intervals, coordinates on a reference path, multiple coordinates in a BED file, a provided subgraph (see User Guide at ??).

### Projecting annotations onto a pangenome

A pangenome represents multiple genomes for which annotations might be available. 
We describe an approach to project annotations relative to a genome onto a pangenome.
We recently updated the `annotate` subcommand from the `vg` toolkit to project regions represented in the BED or GFF files onto the latest pangenomes from the HPRC.
Currently, the genome to annotate must be a *reference* path in the pangenome. 
The `gbwt` subcommand can making a  specific path into a *reference* path in about ?? minutes.
Once a genome or haplotype is a *reference* path, a pangenome can be queried using coordinates on this path.
Internally, `vg annotate` looks for the location of a path in pangenome graph for each input region.
The path, represented as an *alignment* record, is then written either in GAM or GAF formats.
Of note, a path can be broken in multiple disjointed parts.
It happens in the recent human draft pangenome when some regions are clipped out, for example across centromeres or when creating suspiciously large structural variants.
Projected annotations are hence also broken up if needed when they overlap with breakpoints.
The name of the annotated path in the output GAF is picked from the BED file's 4th column, or the *Name* and *ID* GFF field.

We test this approach by projecting the gene annotation, repeat annotations, and segmental duplication annotation for each of the 88 assembled haplotypes in the draft human pangenome from the HPRC (v1.1).
The gene annotations from CAT[@doi:10.1101/gr.233460.117] (GFF files) were downloaded from ??.
The repeat annotations from RepeatMasker (BED files) were downloaded from ??.
The predicted segmental duplications from ?? (BED files) were downloaded from ??.
A helper script was implemented to prepare the BED files with informative names.
For example, for repeats from the RepeatMasker annotation, we name each element by their repeat class and repeat family.
The projection of those annotations for each haplotype was automated with a Snakemake workflow available in the `analysis/annotate` folder of this paper's repository[@repo].

### Coverage track from mapped reads

Functional genomics datasets are often visualized as a coverage track.
High coverage in a region might suggest a strong transcription factor binding site or regulatory region. 

We implemented an approach to summarize the coverage of reads across the pangenome into paths with similar coverage. 
The coverage in every node is first binned into a few coverage classes, for example representing low, medium and high coverage. 
By default we use 1, 5, and 30 reads as coverage breakpoints to save three bins: 1-5, 5-30, 30+. 
Regions with no coverage are not saved.
Once the coverage is binned, we extend greedily to connected nodes and bins if in the same coverage class.
This extension step produces path through the pangenome with consistent coverage. 
The paths are written in the GAF format, recording the coverage class and the average coverage across the path.

![
**Read coverage bin-and-extend approach to produce coarse-grained coverage tracks**
In each node (*grey rectangles*), the read coverage is first binned using user-defined coverage bins (*red blocks*).
Each bin is then extended, one at a time (*green flags*), until reaching a different coverage bin (*red flag*).
](figures/coverage.bin.pangenome.png "Method to make a coverage track from mapped reads"){#fig:meth_cov}

This algorithm was implemented in Python and uses the *libbdsg* module[@libbdsg] to query the pangenome.
It is made available in the public repository of this study in the `analysis/encode` folder of this paper's repository[@repo].

### Annotating known variants

Variants from public databases were annotated when matching a variant site in the pangenome. 
We implemented an approach to look for input variants in the pangenome and write a GAF file with the path followed by those variants in the pangenome. 
The variants are matched with the VCF representation of the HPRC Minigraph-Cactus v1.1 pangenome, produced by running `vg deconstruct` on the pangenome file.
This VCF file contains the all variants and their paths through the pangenome in the *AT* *INFO* field.
We look for the variants of interest in this VCF and extract the appropriate path using the *AT* field.
The annotation path follows either the alternate allele of the variant if known and present in the pangenome, or the reference allele path if the alternate allele is unknown but there is a variant at this position in the pangenome.
Variant that are not matched in the pangenome are skipped.
This algorithm was implemented in Python and uses the *libbdsg* module[@libbdsg] internally to get node size information necessary to write proper GAF records.

We test this approach on the GWAS catalog[@doi:10.1093/nar/gkac1010] and GTEX expression QTLs[@doi:10.1038/ng.2653].
The GWAS catalog was downloaded from the UCSC Genome Browser `gwasCatalog` table[@doi:10.1093/nar/gkac1072 ].
The eQTLs from GTEX v8 were downloaded from `https://storage.googleapis.com/adult-gtex/bulk-qtl/v8/single-tissue-cis-qtl/GTEx_Analysis_v8_eQTL.tar`.
The files defining associations between variant/gene pairs were parsed for each tissue.
As before, the output annotation in GAF were bgzipped, sorted and indexed.

We implemented another, more straightforward approach, to annotate variants that were genotyped using the pangenome.
Here we simply convert a VCF that contain allele traversal information (*AT* field) to a GAF file representing the alternate allele.
We test this approach by genotyping HG002 from short-reads Illumina Novaseq data. `more details`{.red}

The scripts and pipeline to annotate variants is available in the public repository of this study in the `analysis/variants` folder of this paper's repository[@repo].

### Visualization in the sequenceTubeMap

The sequenceTubeMap was develop to interactively explore a pangenome graph, haplotypes traversing it, and reads mapping to it[@tubemap]. 
It internally calls *vg* to extract the relevant slice of the pangenome graph and reads. 
To extract reads, it was only accepting GAM file that had been sorted and indexed *vg*.
We have updated it to accept GAF files that have been sorted, compressed and indexed as explained above.

The new version of the sequenceTubeMap can also display multiple layers of haplotypes or reads. 
As *reads*, the user can now add layers of annotations represented as indexed GAF files.
A different color or color palette can be assigned to each layer to facilitate the visualization of different datasets in the same local pangenome region. 
For example, one could visualize the coding regions of genes and coverage tracks for different cell types from the ENCODE project (Fig ??).

### Visualization in Bandage

A fork of Bandage[@bandage], called BandageNG[@{https://github.com/asl/BandageNG}], can visualize paths of the input graph by coloring the nodes.
We implemented a wrapper script to facilitate the preprocessing of a subgraph to visualize with BandageNG. 
It starts by extracting the subgraph of a full pangenome for a region of interest.
It also extract annotations from indexed files on that same region. 
The annotated paths are then added to the subgraph using `vg augment`. 
The new pangenome subgraph is converted to GFA and contains both the original paths (e.g. haplotypes) and the newly integrated annotations (e.g. gene location, repeats).
The output of this script can be opened with BandageNG for interactive exploration. 
In particular, the *Path search* feature can find nodes corresponding to specific paths, which are either haplotypes or annotations in this pre-processed GFA file.
The user can select a *path*, color the nodes and label the path `check/update`{.red}.
The helper script and a tutorial are available at the `analysis/??`{.red} folder of this paper's repository[@repo].


## Results

### Sorting and indexing short sequencing reads

Read sorting was tested on Illumina HiSeq paired-end short reads for the HG002 sample, each 150 bp long and a genome coverage of about 30X.
The gzipped GAF file with about 682 million reads was sorted in 6h32 using a single thread and about 2Gb of memory (Table @tbl:readsorting_summary).
Indexing the sorted GAF with `tabix` took 18 mins.
We compared that approach with the current implementation in `vg` which uses files in the GAM format.
GAM is a protobuf alignemnt format introduced in Garrison et al.[@vg].
Sorting a GAM with the same reads took 11h47 using a single thread and about 6 Gb of memory. 

In addition to being about twice as fast to sort, reads written in the GAF format (and bgzipped) also take about half the disk space (52G vs 108G).
The main reason for this reduced space is that GAF doesn't save the full read sequence, only the path through the pangenome and edits to reconstruct it.
GAM files produced by `vg giraffe` can also save additional information as annotations, like the mapping time of each read, that are currently not kept when converting to the GAF format.
Overall, the bgzipped GAF files are half as small and twice as fast to sort for short sequencing reads.

Once indexed, extracting a slice of the pangenome is as efficient as extracting a slice of an indexed BAM, VCF, or BED file in a genomic regions, as it uses the same approach.
For example, extracting reads for ten thousand random regions in the pangenome took about 0.07 second per region to retrieve an average of 1707 reads.
For comparison, the same extraction took on average 0.8 second per region using the GAM format. 

| Format | Time (H:M:S) | Max. memory used (Kb) | File size (Gb) |
|:------:|-------------:|----------------------:|---------------:|
| GAM    |     11:46:58 |              6,236.60 |            108 |
| GAF    |      6:50:28 |              1,904.83 |             52 |

Table: Resources used to sort short sequencing reads for a 30x coverage Illumina human dataset.
{#tbl:readsorting_summary}

### Annotation of a human pangenome

Human Pangenome Reference Consotium[@hprc]

To showcase these commands, we projected annotations for all haplotypes in the latest draft human pangenome (HPRC v1.1 GRCh38-based Minigraph-Cactus pangenome). 
This included genes, segmental duplications, tandem repeats and repeats annotations. 
`vg annotate` can annotate ~4M gene annotations in ~16 mins, and ~5.5M repeats from RepeatMasker in ~9 mins on a single-threaded machine. 
Finally, these rich annotations can then be quickly queried with `vg` and visualized using existing tools like the sequenceTubeMap or Bandage.
Using BandageNG, a fork that can import paths in GAF files, paths were searched and colored to illustrate a mobile element insertion.

![
**Visualization examples with BandageNG**
Example of a AluYa5 transposon insertion (*red*) within the coding sequence of the *PRAMEF4* gene (*blue*).
Both annotations were originally produced at the haplotype level by the Human Pangenome Reference Consoritium.
We projected them to the pangenome, indexed them, and queried a small region to visualize with BandageNG.
The nodes were colored based on those annotations, loaded as paths by BandageNG.
](figures/PRAMEF4.AluInsertion.png "Bandage example"){#fig:bandage}

We also matched and annotated more than 660 thousand variants from the GWAS catalog[@doi:10.1093/nar/gkac1010] and expression QTLs from the GTEx catalog[@doi:10.1038/ng.2653] across 49 tissues (on average 1.45 million variants per tissue).
On average, 94% variants were found in the HPRC pangenome.
The variants files in GAF take only 907Mb of space and can be queried fast for visualization in the sequenceTubeMap or Bandage.
This annotation is showcased in example ?? described in more detail below (see *Example??* section).
Of note, it is also straightforward to convert genotypes for variants from the pangenome to annotated paths. 
This could be the case when the pangenome is used as the backbone of the genotyping of new samples, for example with Pangenie or *vg call*.
To illustrate this use case, we genotyped HG002 using short Illumina reads aligned on the draft human pangenome with vg giraffe and vg call.
The predicted genotypes were converted to GAF and indexed.
They could be visualized using the sequenceTubeMap, for example, along with the aligned reads. 
This type of annotation can help a developer explore variant calls and aligned reads. 
A example is shown in figure ?? and described in more details below.
On the traditional reference genome, the equivalent would be to load both reads and variants in IGV[@igv].

![
**Visualization examples with the sequenceTubeMap**
**A** Projection of the HPRC gene annotation, here visualizing a coding sequence (CDS) of the *CFD* gene.
There is an insertion (see *insertion node* in the middle), that the reference path (*violet* on top) skips.
Most CDS annotations are similar (*blue* paths), but the CSD from the haplotype with the insertion seems to be split in two parts, highlighted in *green*.
**B.** Projecting known variants in the pangenome. 
*black*: Reference path (GRCh38), *pale colors*: other human haplotypes, *reds*: GWAS catalog, *blues*: eQTLs across tissues (GTEx).
**C.** Aligned reads and genotype calls.
*yellow*/*green*: annotation paths from `vg call` genotypes. *reds*/*blues*: short sequencing reads.
**D.** ATAC-seq coverage tracks for 7 tissues from the ENCODE project. 
The reference path (*violet*) and other HPRC haplotypes (*greys*) are shown on top and traverse two variation sites.
ATAC-seq coverage track for the different tissues are shown in different *colors* with different opacity representing coverage level.
The thyroid track (*blue*) is more opaque than others suggesting that this region is more open in this tissue.
The *red* tracks at the bottom show the position of exons from the *TPO* gene, a thyroid-specific gene.
](figures/tubemap.examples.png "Tubemap examples"){#fig:tubemap}

Using sequenceTubeMap, haplotypes, read alignments and paths can be visualized interactively. 

### Coverage of seven functional datasets from ENCODE

We aligned ATAC-seq datasets from 7 cell types to the draft human pangenome to produce coverage tracks as indexed GAF files. 
On average, there were about 475 thousand paths representing high read coverage which were 2.6 nodes (104.8 bases) long. 
On average, 63 thousand paths with high ATAC-seq read coverage traversed more three or more nodes, i.e. regions of the pangenome with variation (see Table @tbl:coverage_summary).

| Dataset                    |   Paths | Average bases | Average nodes | Traversing >2 nodes |
|:---------------------------|--------:|--------------:|--------------:|--------------------:|
| Breast epithelium          | 570,155 |        109.80 |          2.68 |      65,095 (11.4%) |
| Gastrocnemius medialis     | 342,830 |         94.47 |          2.43 |      53,595 (15.6%) |
| Gastroesophageal sphincter | 555,618 |        115.69 |          2.73 |        72,407 (13%) |
| Peyer’s patch              | 270,094 |         97.88 |          2.62 |      43,591 (16.1%) |
| Sigmoid colon              | 678,380 |        115.10 |          2.69 |      82,906 (12.2%) |
| Spleen                     | 531,910 |        104.97 |          2.66 |      67,153 (12.6%) |
| Thyroid gland              | 377,157 |         95.63 |          2.41 |        56,441 (15%) |

Table: High coverage tracks from seven functional datasets on the HPRC pangenome. For each sample, the table shows how many paths had a mean coverage of at least 10 reads, and how long they were.
{#tbl:coverage_summary}

It took on average 7 cpu.hours to map the reads to the pangenome using VG Giraffe, and 2.8 cpu.hours to produce the coverage tracks.
Sorting, compressing and indexing them took only 0.23 cpu.hours, on average.
Table @tbl:coverage_benchmark compiles the runtimes and memory used for each step across all samples.

`example of what we could look for and describe`{.red}
Fig @fig:cov_examples shows examples of those tracks visualized using the sequenceTubeMap.
In Fig ??a, the promoter of the *??* gene is seen to be open in the ?? cell type. 
Thanks to the pangenomic view, we see differential coverage of the functional tracks across the variants in the region.
For instance, we notice a small insertion-deletion (indel) where the alternate allele is only covered by 2 reads, while the reference allele is covered by more than 30 reads.
Fig ??b highlights a structural variant, a ??bp insertion, that is highly covered by ATAC-seq in several cell types.
The RepeatMasker annotation in this region, also extracted from an indexed GAF file, flags this insertion as a ?? transposable element.
?? can indeed attract TF?? that lead to open chromatin ?REF?.

<!-- ![ -->
<!-- **Coverage tracks visualized interactively using the sequenceTubeMap.** -->
<!-- a) Promoter... b) Structural variant.... -->
<!-- ](figures/wide.png "Wide image"){#fig:cov_examples} -->


## Discussion

The tools and applications described here present an option to streamline the production of annotations in the GAF format, their indexing and efficient querying.
First, these techniques will help integrate additional information into existing or future pangenomic tools.
They will simplify the integration of information like gene or repeat annotations, known variants, or more generally other functional annotations, in pangenomic analysis.
These analysis will be able to work with those annotations in light of underlying genomic variation recapitulated in the pangenome.
Visualization is a specific example where the users typically want to include several layer of annotations, including some custom-made.
Tools to visualize pangenomes will greatly benefit from a simple pipeline to create or load pangenomic annotations.
Second, this work is critical to allow the community to make, share and reuse annotations in the pangenome space.
The GAF format is already used by multiple independent tools, although mostly read mappers.
Thanks to our work, GAF files can now be indexed and queried efficiently, like BED, VCF, or GFF on a linear reference genome. 
We also showcase how annotations on a linear genome can be converted to a path in the pangenome in the GAF format.
For these reasons, we believe it could become the de facto format to represent annotations in the pangenome and accelerate the adoption of the new pangenomic paradigm by the broader genomics field.
Although informative annotations could be analyzed already, the current approach has some limitations.
<!-- - Simplistic handling of clipped paths. -->

The indexing scheme relies on integer node IDs, compacted relative to their position in the pangenome.
If node IDs are not integer, it adds a layer of complexity for the user as they will need to convert them to integers and keep track of the translation between original pangenome and new pangenome.
Both `vg` and `odgi` offer ways to convert pangenome to a new pangenome with compact integer node IDs.

The current implementation is designed with short paths in mind, where the user wants to extract the full annotated paths in a region.
It is convenient when working with short reads, gene annotations, and most genomic repeats, for example.
Larger genomic regions, like chromosome bands, large assembled contigs, or large segmental duplications, can still be represented and manipulated, but might be less practical to work with.
With the current implementation, the full annotated region will be extracted when querying an overlapping region.
The extracted annotations are not clipped to the specified range which could be inconvenient to a user who zooming into a small region but would still like to know about the much larger annotated path traversing this subgraph.
To address this use case, we plan to implement an extraction mode where output annotations are trimmed to keep only the queried subgraph.

The naive metadata integration is another limitation.
Indeed, the annotation information is currently reduced to a single label.
In our applications, those label would contain for example a gene name and haplotype names, or a read coverage bin and average coverage value, all in one label.
This was easy to implement and sufficient for now because there are no tools that handle more advanced metadata organization.
For many annotations, it would be useful to keep the metadata better organized, so that the user can access/use it within visualization tools.
The different metadata could be saved using optional tags that can be added at the end of each GAF record.

Our approach to convert annotations from a linear genome to the pangenome assumes that we have annotations of the different haplotypes in the pangenome.
There is still no clear solution to lift annotations from one reference/haplotype to other haplotypes in the pangenome, except through reanalysis/reannotation of each haplotype.
The homology information embedded in the pangenome could potentially be used to propagate annotations from one haplotype to others more easily. 
This strategy can already be used by annotation tools like CAT[@doi:10.1101/gr.233460.117], as a additional source of gene annotation evidence.
In the future, these techniques might help propagate other types of annotations across the pangenome more efficiently than by reanalyzing the raw data from scratch on each haplotype.
`something about odgi paths/untangle maybe`{.red}

It also highlights the limitations of the existing tools to integrate these files.
Some tools, like Bandage or GfaViz, require manual pre-processing, for example extracting a subgraph and integrating the annotations as embedded paths.
The sequenceTubeMap can now handle indexed bgzipped GAF files, but the query time for large pangenome remains long in practice.
Defining and integrating annotation metadata into its interface will also require a significant amount of development.
Overall, we stress the need for visualization tools that can efficiently layout and organize many paths through a pangenome.

We showed that the GAF format, thanks to new tools for their efficient manipulation, could offer a path for the future of annotations in pangenome graphs.
While it provides an important building block, it is clear that more needs to be done to make it a useful solution for the community.


## Code and data availability

`vg` is available at [https://github.com/vgteam/vg](https://github.com/vgteam/vg).
The fork of Bandage that allow for path coloring is available at [https://github.com/asl/BandageNG](https://github.com/asl/BandageNG).
The sequenceTubeMap is hosted at [https://github.com/vgteam/sequenceTubemap](https://github.com/vgteam/sequenceTubemap)

The analysis presented in this manuscript is documented in the [https://github.com/jmonlong/manu-vggafannot](https://github.com/jmonlong/manu-vggafannot).
It contains scripts used to prepare the annotation files, commands and automated pipelines used to annotate them in the pangenome, and helper scripts to summarize the output files.

The annotations of the HPRC v1.1 pangenome were deposited on Zenodo at `??ZENODO_LINK??`{.red}.
This includes gene annotations, repeats from RepeatMasker, simple repeats and segmental duplications.
Coverage tracks for the `??` ENCODE ATAC-seq samples are also available in this repository.


## References {.page_break_before}

[@vg]: doi:10.1038/nbt.4227
[@giraffe]: doi:10.1126/science.abg8871
[@vgsv]: doi:10.1186/s13059-020-1941-7
[@hapsamp]: doi:10.1101/2023.12.13.571553 
[@libbdsg]: doi:10.1093/bioinformatics/btaa640
[@hprc]: doi:10.1038/s41586-023-05896-x
[@tubemap]: doi:10.1093/bioinformatics/btz597
[@bandage]: doi:10.1093/bioinformatics/btv383
[@minigraph]: doi:10.1186/s13059-020-02168-z
[@minigraph_cactus]: doi:10.1038/s41587-023-01793-w
[@odgi]: doi:10.1093/bioinformatics/btac308
[@layout]: doi:10.1093/bioinformatics/btae363
[@pggb]: doi:10.1101/2023.04.05.535718
[@htslib]: doi:10.1093/gigascience/giab007
[@tabix]: doi:10.1093/bioinformatics/btq671
[@igv]: doi:10.1038/nbt.1754
[@repo]: https://github.com/jmonlong/manu-vggafannot

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>


## Supplementary material {.page_break_before}


| Dataset                    | reads (M) |      read mapping |     coverage track | sorting + compressing + indexing |
|:---------------------------|----------:|------------------:|-------------------:|---------------------------------:|
| Breast epithelium          |     193.6 | 8.9 cpu.h (54 Gb) | 3.1 cpu.h (108 Gb) |                 0.2 cpu.h (1 Gb) |
| Gastrocnemius medialis     |      98.8 | 4.8 cpu.h (54 Gb) | 2.4 cpu.h (100 Gb) |                 0.1 cpu.h (1 Gb) |
| Gastroesophageal sphincter |     168.5 | 7.3 cpu.h (54 Gb) | 2.7 cpu.h (107 Gb) |                 0.2 cpu.h (1 Gb) |
| Peyer's patch              |     145.3 |   8 cpu.h (54 Gb) | 2.6 cpu.h (104 Gb) |                 0.2 cpu.h (1 Gb) |
| Sigmoid colon              |     173.5 | 8.2 cpu.h (54 Gb) | 2.7 cpu.h (104 Gb) |                 0.2 cpu.h (1 Gb) |
| Spleen                     |     157.2 | 7.6 cpu.h (54 Gb) | 2.8 cpu.h (105 Gb) |                 0.2 cpu.h (1 Gb) |
| Thyroid gland              |      91.4 | 4.6 cpu.h (54 Gb) |  2.3 cpu.h (94 Gb) |                 0.1 cpu.h (1 Gb) |

Table: `update`{.red} Compute resources used for the analysis of the functional datasets and production of the indexed coverage tracks.
{#tbl:coverage_benchmark}

