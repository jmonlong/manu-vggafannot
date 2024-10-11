
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
bm.df %>% group_by(task) %>% summarize(cpu_h=mean(cpu_time/3600),
                                       cpu_m=mean(cpu_time/60),
                                       min=mean(s/60),
                                       mean_load=mean(mean_load),
                                       max_rss=mean(max_rss),
                                       max_rss_gib=max_rss/1024) %>%
  kable(format.args=list(big.mark=','))
```

| task                              |      cpu_h |       cpu_m |        min | mean_load |   max_rss | max_rss_gib |
|:----------------------------------|-----------:|------------:|-----------:|----------:|----------:|------------:|
| HG002.count_kmer_in_reads.tsv     |  1.3031528 |    78.18917 |  13.814610 |    566.00 | 61,153.05 |   59.719775 |
| HG002.gam_to_gaf.tsv              | 12.0370139 |   722.22083 | 182.512272 |    395.71 |  8,648.95 |    8.446240 |
| HG002.index_distance.tsv          |  0.1932861 |    11.59717 |  12.318207 |     94.09 | 54,274.38 |   53.002324 |
| HG002.index_gaf.tsv               |  0.2903167 |    17.41900 |  18.560872 |     93.83 |      5.42 |    0.005293 |
| HG002.index_minimizer.tsv         |  0.3525222 |    21.15133 |   3.720128 |    567.39 | 45,915.90 |   44.839746 |
| HG002.map_short_reads_giraffe.tsv | 41.5747917 | 2,494.48750 | 158.599967 |  1,572.82 | 47,329.29 |   46.220010 |
| HG002.sample_haplotypes.tsv       |  0.3253667 |    19.52200 |   5.673115 |    344.24 | 29,072.87 |   28.391475 |
| HG002.sort_gaf.tsv                |  6.4707667 |   388.24600 | 392.477480 |     98.92 |  1,904.83 |    1.860186 |
| HG002.sort_gam.tsv                | 11.6469083 |   698.81450 | 706.980093 |     98.84 |  6,236.60 |    6.090430 |
