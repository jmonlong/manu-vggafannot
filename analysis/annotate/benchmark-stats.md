
``` r
library(dplyr)
```

    ## 
    ## Attaching package: 'dplyr'

    ## The following objects are masked from 'package:stats':
    ## 
    ##     filter, lag

    ## The following objects are masked from 'package:base':
    ## 
    ##     intersect, setdiff, setequal, union

``` r
library(knitr)
library(tidyr)
```

## Benchmark files produced by snakemake

``` r
bm.df = lapply(list.files('benchmark'), function(fpath){
  df = read.table(paste0('benchmark/', fpath), as.is=TRUE, sep='\t', header=TRUE)
  df$task = gsub('.tsv', '', fpath)
  df
}) %>% bind_rows

bm.df = bm.df %>% mutate(sample=gsub("[^\\.]+\\.(.+).benchmark", "\\1", task),
                         task=gsub("([^\\.])\\..+.benchmark", "\\1", task)) %>%
  select(task, sample, everything())
```

### Average resources per task

``` r
bm.df %>% group_by(task) %>% summarize(cpu_h=mean(cpu_time/3600),
                                       min=mean(s/60),
                                       mean_load=mean(mean_load),
                                       max_rss=mean(max_rss)) %>%
  kable(format.args=list(big.mark=','))
```

| task                |     cpu_h |         min | mean_load |       max_rss |
|:--------------------|----------:|------------:|----------:|--------------:|
| extract_type        | 0.0126569 |   1.0613455 |  71.18869 |     29.621307 |
| index_gaf           | 0.0013864 |   0.1005908 |  40.56852 |      5.772188 |
| merge_rm.benchmark  | 3.5995944 | 219.1225467 |  98.45000 |  2,121.120000 |
| merge_trf.benchmark | 0.3510611 |  22.2491667 |  94.42000 |  2,410.190000 |
| merge_type          | 0.2600917 |  16.5907542 |  91.17500 |  1,724.155000 |
| prep_cat_gene       | 0.0211708 |   1.6672916 |  75.95341 |     18.620682 |
| prep_haplotype_gbz  | 0.0126468 |   0.9048961 |  84.02409 | 13,574.914545 |
| prep_repeat_masker  | 0.0044667 |   0.3835808 |  68.71898 |     18.582954 |
| prep_segdups        | 0.0002160 |   0.0272063 |  31.83886 |     18.593295 |
| prep_trf_repeats    | 0.0019865 |   0.1404085 |  81.88784 |     24.880796 |
| sort_gaf            | 0.0186279 |   1.2979269 |  80.64284 |  2,078.421420 |
| vg_annotate         | 0.1163320 |   3.9076271 | 162.84111 | 21,299.568807 |
