
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

bm.df = bm.df %>%
  mutate(sample=gsub("[^\\.]+\\.(.+)", "\\1", task),
         task=gsub("([^\\.])\\..+", "\\1", task),
         task=ifelse(task=='HG002', sample, task)) %>%
  select(task, sample, everything())
```

### Average resources per task

``` r
bm.df %>% group_by(task) %>% summarize(cpu_h=mean(cpu_time/3600),
                                       min=mean(s/60),
                                       mean_load=mean(mean_load),
                                       max_rss=mean(max_rss),
                                       max_rss_gib=max_rss/1024) %>%
  kable(format.args=list(big.mark=','))
```

| task | cpu_h | min | mean_load | max_rss | max_rss_gib |
|:---|---:|---:|---:|---:|---:|
| annotate_calls | 0.0017250 | 0.1090900 | 87.080000 | 4,302.380000 | 4.2015430 |
| annotate_eqtls | 0.0068884 | 0.6908005 | 55.509388 | 4,965.226735 | 4.8488542 |
| annotate_gwas | 0.0043500 | 0.4910917 | 51.330000 | 4,595.820000 | 4.4881055 |
| genotype_vg_call.tsv | 2.9871694 | 62.8227667 | 285.290000 | 61,094.090000 | 59.6621973 |
| index_gaf | 0.0000710 | 0.0083024 | 3.533726 | 6.788824 | 0.0066297 |
| pack_read_cov.tsv | 4.2825194 | 68.2456250 | 376.510000 | 43,065.980000 | 42.0566211 |
| sort_gaf | 0.0025661 | 0.1268313 | 107.058431 | 657.553137 | 0.6421417 |
