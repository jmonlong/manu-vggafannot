
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
library(ggplot2)
library(tidyr)
library(knitr)
```

## Read benchmarking files

``` r
nregs = 20
reg_size = c(100, 1000, 10000)

df = lapply(reg_size, function(rs){
  read.table(paste0('benchmark.query.', nregs, '.', rs, '.tsv'), header=TRUE, sep='\t', comment='') %>%
    mutate(size=rs)
}) %>% bind_rows

sample_n(df, 3) %>% select(size, method, region, s)
```

    ##    size         method                            region        s
    ## 1   100             vg  GRCh38#0#chr18:30339677-30339777 33.59794
    ## 2 10000 chunkix_remote  GRCh38#0#chr17:13249195-13259195 12.04265
    ## 3 10000 chunkix_remote GRCh38#0#chr7:150869665-150879665 20.14897

Annotate the query number to check if the first query takes longer for
remote files (because of the time it takes to download the tbi files).

``` r
df = df %>% group_by(size) %>%
  mutate(query.nb=as.numeric(factor(region, levels=unique(region))))
```

## Query time distribution

``` r
ggplot(df, aes(x=factor(size), y=s, fill=method)) +
  geom_point(data=subset(df, query.nb==1), size=3, alpha=1,
             position=position_dodge(.75), shape=5) + 
  geom_boxplot(position='dodge') + theme_bw() +
  xlab('region size (bp)') + coord_flip() +
  scale_fill_brewer(palette='Set2') +
  theme(legend.position='bottom') + 
  ylab('query time (s)')
```

![](query.time.test_files/figure-gfm/query_time-1.png)<!-- -->

The diamond highlights the first query. When querying remote files, the
first query takes more time because the tbi files need to be downloaded.

``` r
df %>% filter(method=='chunkix_remote') %>%
  group_by(size) %>% summarize(med.s=median(s), first.s=s[query.nb==1]) %>%
  mutate(first.penalty.s=first.s-med.s) %>% kable
```

|  size |    med.s |  first.s | first.penalty.s |
|------:|---------:|---------:|----------------:|
|   100 | 15.43305 | 33.38279 |        17.94973 |
|  1000 | 16.03757 | 44.10231 |        28.06474 |
| 10000 | 13.99856 | 34.39622 |        20.39767 |

Downloading the tbi files adds about 20 seconds in our case

Note: this remote query was performed from France and accessing index
files hosted in a server in Santa Cruz, California.

## Summary table

Average query time per method and region size.

``` r
df %>% group_by(method, size) %>%
  summarize(s=mean(s, na.rm=TRUE), .groups='drop') %>%
  pivot_wider(names_from=method, values_from=s) %>%
  kable
```

|  size |   chunkix | chunkix_remote |       vg |
|------:|----------:|---------------:|---------:|
|   100 | 0.4868282 |       16.24498 | 33.26382 |
|  1000 | 0.4965837 |       17.37299 | 33.37983 |
| 10000 | 0.4763262 |       15.90399 | 33.39566 |
