---
title: Current options to index, represent, and visualize annotations in a pangenome with the vg toolkit
keywords:
- pangenome
- annotation
- alignment
lang: en-US
date-meta: '2024-08-22'
author-meta:
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
  <meta name="dc.date" content="2024-08-22" />
  <meta name="citation_publication_date" content="2024-08-22" />
  <meta property="article:published_time" content="2024-08-22" />
  <meta name="dc.modified" content="2024-08-22T15:20:11+00:00" />
  <meta property="article:modified_time" content="2024-08-22T15:20:11+00:00" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Jean Monlong" />
  <meta name="citation_author_institution" content="IRSD - Digestive Health Research Institute, University of Toulouse, INSERM, INRAE, ENVT, UPS, Toulouse, France" />
  <meta name="citation_author_orcid" content="0000-0002-9737-5516" />
  <link rel="canonical" href="https://jmonlong.github.io/manu-vggafannot/" />
  <meta property="og:url" content="https://jmonlong.github.io/manu-vggafannot/" />
  <meta property="twitter:url" content="https://jmonlong.github.io/manu-vggafannot/" />
  <meta name="citation_fulltext_html_url" content="https://jmonlong.github.io/manu-vggafannot/" />
  <meta name="citation_pdf_url" content="https://jmonlong.github.io/manu-vggafannot/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://jmonlong.github.io/manu-vggafannot/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://jmonlong.github.io/manu-vggafannot/v/8989ca090be2e645b72a31cf0e85157025f63926/" />
  <meta name="manubot_html_url_versioned" content="https://jmonlong.github.io/manu-vggafannot/v/8989ca090be2e645b72a31cf0e85157025f63926/" />
  <meta name="manubot_pdf_url_versioned" content="https://jmonlong.github.io/manu-vggafannot/v/8989ca090be2e645b72a31cf0e85157025f63926/manuscript.pdf" />
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
([permalink](https://jmonlong.github.io/manu-vggafannot/v/8989ca090be2e645b72a31cf0e85157025f63926/))
was automatically generated
from [jmonlong/manu-vggafannot@8989ca0](https://github.com/jmonlong/manu-vggafannot/tree/8989ca090be2e645b72a31cf0e85157025f63926)
on August 22, 2024.
</em></small>



## Authors



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
To enable similar enrichment of a pangenome reference, there is a dire need for tools and formats for pangenomic annotation. 
Simple text formats, like VCF or BED, have been widely adopted and helped this critical exchange of genomic information. 
The Graph Alignment Format (GAF) text format, which was proposed to represent alignments, could be used to represent any type of annotation in a pangenome graph.
Here I review how some features of the `vg` ecosystem can already provide indexing, querying, and visualization capabilities for annotations represented as paths.

We developed efficient sorting, indexing and querying for GAF files.
This approach can for example extract annotations overlapping a subgraph quickly.
Alignments are currently sorted based on the covered node IDs, similar to the approach for sorting read alignments in the GAM format, a binary format used previously by the `vg` toolkit. 
To index the bgzipped GAF file, we extended HTSlib/tabix to work with the GAF format. 
Second, `vg annotate` was recently updated to better produce graph annotations as paths, starting from annotation files relative to linear references. 
More precisely, it can to take annotations in BED or GFF3 files, written relative to reference paths or haplotypes, and produce GAF files representing the equivalent paths through the pangenome.

To showcase these commands, we projected annotations for all haplotypes in the latest draft human pangenome (HPRC v1.1 GRCh38-based Minigraph-Cactus pangenome). 
This included genes, segmental duplications, tandem repeats and repeats annotations. 
`vg annotate` can annotate ~4M gene annotations in ~16 mins, and ~5.5M repeats from RepeatMasker in ~9 mins on a single-threaded machine. 
Finally, these rich annotations can then be quickly queried with `vg` and visualized using existing tools like the sequenceTubeMap or Bandage.




## References {.page_break_before}

[@giraffe]: doi:10.1126/science.abg8871
[@hprc]: doi:10.1038/s41586-023-05896-x


<!-- Explicitly insert bibliography here -->
<div id="refs"></div>

