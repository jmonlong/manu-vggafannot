
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
  df$task = gsub('.benchmark.tsv', '', fpath)
  df
}) %>% bind_rows
```

### Average resources per task

``` r
bm.df %>% mutate(cpu_h=cpu_time/3600,
                 cpu_m=cpu_time/60,
                 max_rss_gib=max_rss/1024) %>%
  select(task, h.m.s, cpu_h, cpu_m, mean_load, max_rss, max_rss_gib) %>% 
  kable(format.args=list(big.mark=','))
```

| task | h.m.s | cpu_h | cpu_m | mean_load | max_rss | max_rss_gib |
|:---|:---|---:|---:|---:|---:|---:|
| HG002.count_kmer_in_reads.tsv | 0:13:48 | 1.3031528 | 78.18917 | 566.00 | 61,153.05 | 59.7197754 |
| HG002.gam_to_gaf.tsv | 4:40:29 | 18.5188694 | 1,111.13217 | 396.13 | 8,608.69 | 8.4069238 |
| HG002.index_distance.tsv | 0:12:19 | 0.1932861 | 11.59717 | 94.09 | 54,274.38 | 53.0023242 |
| HG002.index_gaf.tsv | 0:20:55 | 0.3068278 | 18.40967 | 87.97 | 5.84 | 0.0057031 |
| HG002.index_minimizer.tsv | 0:03:43 | 0.3525222 | 21.15133 | 567.39 | 45,915.90 | 44.8397461 |
| HG002.map_short_reads_giraffe.tsv | 2:38:35 | 41.5747917 | 2,494.48750 | 1,572.82 | 47,329.29 | 46.2200098 |
| HG002.sample_haplotypes.tsv | 0:05:40 | 0.3253667 | 19.52200 | 344.24 | 29,072.87 | 28.3914746 |
| HG002.sort_gaf_mt.tsv | 1:16:28 | 3.8987139 | 233.92283 | 305.86 | 1,718.68 | 1.6783984 |
| HG002.sort_gaf.tsv | 3:55:13 | 3.8792833 | 232.75700 | 98.95 | 856.61 | 0.8365332 |
| HG002.sort_gam.tsv | 12:00:19 | 11.8777444 | 712.66467 | 98.94 | 7,146.33 | 6.9788379 |
