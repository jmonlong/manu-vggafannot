
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
         task=gsub("([^\\.])\\..+", "\\1", task)) %>%
  select(task, sample, everything())
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

| task | cpu_h | cpu_m | min | mean_load | max_rss | max_rss_gib |
|:---|---:|---:|---:|---:|---:|---:|
| extract_type | 0.0126569 | 0.7594129 | 1.0613455 | 71.18869 | 29.621307 | 0.0289271 |
| index_gaf | 0.0013864 | 0.0831847 | 0.1005908 | 40.56852 | 5.772188 | 0.0056369 |
| merge_rm | 3.5995944 | 215.9756667 | 219.1225467 | 98.45000 | 2,121.120000 | 2.0714062 |
| merge_trf | 0.3510611 | 21.0636667 | 22.2491667 | 94.42000 | 2,410.190000 | 2.3537012 |
| merge_type | 0.2600917 | 15.6055000 | 16.5907542 | 91.17500 | 1,724.155000 | 1.6837451 |
| prep_cat_gene | 0.0211708 | 1.2702500 | 1.6672916 | 75.95341 | 18.620682 | 0.0181843 |
| prep_haplotype_gbz | 0.0126468 | 0.7588068 | 0.9048961 | 84.02409 | 13,574.914545 | 13.2567525 |
| prep_repeat_masker | 0.0044667 | 0.2680000 | 0.3835808 | 68.71898 | 18.582954 | 0.0181474 |
| prep_segdups | 0.0002160 | 0.0129621 | 0.0272063 | 31.83886 | 18.593295 | 0.0181575 |
| prep_trf_repeats | 0.0019865 | 0.1191913 | 0.1404085 | 81.88784 | 24.880796 | 0.0242977 |
| sort_gaf | 0.0186279 | 1.1176714 | 1.2979269 | 80.64284 | 2,078.421420 | 2.0297084 |
| vg_annotate | 0.1163320 | 6.9799181 | 3.9076271 | 162.84111 | 21,299.568807 | 20.8003602 |

## Average per input type for the `vg annotate` task

``` r
bm.df %>% filter(task=='vg_annotate') %>% mutate(input=gsub('(.+)_.+', '\\1', sample)) %>%
  group_by(input) %>% summarize(cpu_h=mean(cpu_time/3600),
                                cpu_m=mean(cpu_time/60),
                                min=mean(s/60),
                                mean_load=mean(mean_load),
                                max_rss=mean(max_rss),
                                max_rss_gib=max_rss/1024) %>%
  kable(format.args=list(big.mark=','))
```

| input |     cpu_h |     cpu_m |        min | mean_load |   max_rss | max_rss_gib |
|:------|----------:|----------:|-----------:|----------:|----------:|------------:|
| gene  | 0.3313188 | 19.879127 | 10.5568126 |  189.2862 | 21,412.55 |    20.91069 |
| rm    | 0.0813806 |  4.882837 |  2.8609341 |  171.0506 | 21,202.97 |    20.70603 |
| sd    | 0.0260668 |  1.564010 |  0.9987033 |  158.6775 | 21,336.03 |    20.83597 |
| trf   | 0.0265616 |  1.593699 |  1.2140585 |  132.3501 | 21,246.72 |    20.74875 |
