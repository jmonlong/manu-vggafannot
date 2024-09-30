
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

bm.df = bm.df %>% mutate(sample=gsub(".+\\.(.+)", "\\1", task),
                         task=gsub("(.+)\\..+", "\\1", task)) %>%
  select(task, sample, everything())
kable(bm.df)
```

| task | sample | s | h.m.s | max_rss | max_vms | max_uss | max_pss | io_in | io_out | mean_load | cpu_time |
|:---|:---|---:|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| convert_gbz_to_pg | convert_gbz_to_pg | 293.4269 | 0:04:53 | 13807.30 | 19176.97 | 13807.35 | 13807.35 | 9.30 | 0.00 | 98.39 | 288.94 |
| index_gaf | breast_epithelium | 22.9293 | 0:00:22 | 5.34 | 12.61 | 3.51 | 4.54 | 2.15 | 0.00 | 67.05 | 15.63 |
| index_gaf | gastrocnemius_medialis | 26.8872 | 0:00:26 | 5.36 | 12.61 | 3.45 | 4.62 | 2.22 | 0.00 | 29.46 | 7.97 |
| index_gaf | gastroesophageal_sphincter | 22.0024 | 0:00:22 | 5.43 | 12.61 | 3.66 | 4.67 | 2.15 | 0.00 | 70.07 | 15.67 |
| index_gaf | PeyersPatch | 17.5413 | 0:00:17 | 5.43 | 12.61 | 3.51 | 4.60 | 2.15 | 0.00 | 86.83 | 15.45 |
| index_gaf | sigmoid_colon | 20.0628 | 0:00:20 | 5.29 | 12.61 | 3.33 | 4.44 | 2.15 | 0.00 | 76.82 | 15.64 |
| index_gaf | spleen | 31.7643 | 0:00:31 | 5.34 | 25.21 | 3.32 | 4.46 | 2.15 | 0.00 | 24.87 | 7.94 |
| index_gaf | thyroid_gland | 10.2998 | 0:00:10 | 5.20 | 12.61 | 3.39 | 4.55 | 2.15 | 0.00 | 77.73 | 8.33 |
| make_cov | breast_epithelium | 6489.2011 | 1:48:09 | 111251.02 | 205968.81 | 111248.07 | 111249.50 | 1759.06 | 0.00 | 165.05 | 10711.08 |
| make_cov | gastrocnemius_medialis | 6173.4309 | 1:42:53 | 101179.16 | 190254.70 | 101176.10 | 101177.56 | 513.06 | 0.00 | 150.86 | 9313.34 |
| make_cov | gastroesophageal_sphincter | 6860.0337 | 1:54:20 | 110522.17 | 203984.40 | 110519.01 | 110520.46 | 2657.46 | 0.00 | 155.75 | 10684.77 |
| make_cov | PeyersPatch | 7235.6699 | 2:00:35 | 106392.37 | 195852.16 | 106389.46 | 106390.94 | 24.36 | 0.00 | 147.63 | 10682.48 |
| make_cov | sigmoid_colon | 7020.9373 | 1:57:00 | 108125.57 | 202588.34 | 108122.43 | 108123.93 | 1411.37 | 0.00 | 155.06 | 10887.46 |
| make_cov | spleen | 6646.7884 | 1:50:46 | 106966.43 | 201385.10 | 106963.21 | 106964.75 | 16.86 | 0.00 | 160.43 | 10663.78 |
| make_cov | thyroid_gland | 5966.9777 | 1:39:26 | 95781.10 | 184888.95 | 95778.20 | 95779.74 | 16.86 | 0.00 | 151.17 | 9020.57 |
| map_reads | breast_epithelium | 4251.8955 | 1:10:51 | 55581.25 | 104949.44 | 55587.25 | 55588.14 | 47960.77 | 0.00 | 754.67 | 32088.55 |
| map_reads | gastrocnemius_medialis | 2462.8905 | 0:41:02 | 55692.81 | 104645.94 | 47401.83 | 51548.60 | 20974.76 | 0.00 | 700.66 | 17257.11 |
| map_reads | gastroesophageal_sphincter | 3436.8709 | 0:57:16 | 55712.97 | 104758.94 | 47419.71 | 51566.42 | 1089.15 | 0.00 | 763.49 | 26240.65 |
| map_reads | PeyersPatch | 3998.0724 | 1:06:38 | 55761.16 | 105003.94 | 55715.89 | 55716.79 | 2699.95 | 0.00 | 717.50 | 28686.33 |
| map_reads | sigmoid_colon | 3858.0162 | 1:04:18 | 55612.79 | 105033.94 | 55582.70 | 55583.62 | 11093.99 | 0.00 | 765.08 | 29517.25 |
| map_reads | spleen | 3707.6335 | 1:01:47 | 55714.13 | 104751.44 | 55719.32 | 55720.22 | 25438.74 | 0.00 | 735.76 | 27279.73 |
| map_reads | thyroid_gland | 2265.1633 | 0:37:45 | 55569.54 | 104830.94 | 47287.90 | 50052.71 | 4799.28 | 0.00 | 725.23 | 16428.36 |
| sort_cov_gaf | breast_epithelium | 1042.9505 | 0:17:22 | 909.60 | 1196.36 | 908.77 | 909.95 | 9.68 | 4776.93 | 99.34 | 1036.12 |
| sort_cov_gaf | gastrocnemius_medialis | 1094.2870 | 0:18:14 | 1003.07 | 1324.23 | 1002.25 | 1003.37 | 9.68 | 2697.54 | 97.16 | 1063.31 |
| sort_cov_gaf | gastroesophageal_sphincter | 875.1840 | 0:14:35 | 919.47 | 1196.23 | 918.58 | 919.77 | 9.68 | 4406.07 | 97.56 | 854.05 |
| sort_cov_gaf | PeyersPatch | 753.0436 | 0:12:33 | 925.54 | 1196.36 | 924.43 | 925.68 | 9.76 | 3827.16 | 114.72 | 864.16 |
| sort_cov_gaf | sigmoid_colon | 958.6938 | 0:15:58 | 921.51 | 1196.36 | 920.45 | 921.66 | 9.68 | 4165.71 | 98.76 | 946.90 |
| sort_cov_gaf | spleen | 636.8579 | 0:10:36 | 921.44 | 1196.36 | 920.36 | 921.64 | 9.68 | 3865.53 | 115.85 | 738.04 |
| sort_cov_gaf | thyroid_gland | 291.7329 | 0:04:51 | 933.61 | 1196.36 | 932.57 | 933.81 | 9.68 | 1905.95 | 120.27 | 351.35 |

## Number of reads

Computed by the snakemake pipeline

``` r
rc.df = lapply(list.files('results', 'wc', recursive=TRUE), function(fn){
  tibble(sample=gsub('.*/(.*).gaf.wc.txt', '\\1', fn),
         read=scan(paste0('results/', fn), 1, quiet=TRUE))
}) %>% bind_rows
kable(rc.df)
```

| sample                     |      read |
|:---------------------------|----------:|
| breast_epithelium          | 193556762 |
| gastrocnemius_medialis     |  98841242 |
| gastroesophageal_sphincter | 168481212 |
| PeyersPatch                | 145258696 |
| sigmoid_colon              | 173532518 |
| spleen                     | 157220976 |
| thyroid_gland              |  91374726 |

## Summary table

### Average resources per task

``` r
bm.df %>% group_by(task) %>% summarize(cpu_h=mean(cpu_time/3600),
                                       h=mean(s/3600),
                                       mean_load=mean(mean_load),
                                       max_rss=mean(max_rss)) %>%
  kable(format.args=list(big.mark=','))
```

| task              |     cpu_h |         h | mean_load |      max_rss |
|:------------------|----------:|----------:|----------:|-------------:|
| convert_gbz_to_pg | 0.0802611 | 0.0815075 |  98.39000 | 1.380730e+04 |
| index_gaf         | 0.0034377 | 0.0060114 |  61.83286 | 5.341429e+00 |
| make_cov          | 2.8556937 | 1.8409936 | 155.13571 | 1.057454e+05 |
| map_reads         | 7.0435706 | 0.9516088 | 737.48429 | 5.566352e+04 |
| sort_cov_gaf      | 0.2322988 | 0.2243155 | 106.23714 | 9.334629e+02 |

### Summary for each sample

``` r
samp.levs = c("breast_epithelium", "gastrocnemius_medialis", "gastroesophageal_sphincter",
              "PeyersPatch", "sigmoid_colon", "spleen", "thyroid_gland")
samp.labs = c("Breast epithelium", "Gastrocnemius medialis", "Gastroesophageal sphincter",
              "Peyer's patch", "Sigmoid colon", "Spleen", "Thyroid gland")

merge(bm.df, rc.df) %>%
  mutate(res=paste0(round(cpu_time/3600, 1), ' cpu.h (', round(max_rss/1024), ' Gb)'),
         read=round(read/1e6, 1),
         task=factor(task,
                     c('make_cov', 'map_reads', 'sort_cov_gaf'),
                     c('coverage track', 'read mapping', 'sorting + compressing + indexing')),
         sample=factor(sample, samp.levs, samp.labs)) %>%
  filter(!is.na(task)) %>%
  select(sample, read, task, res) %>% 
  pivot_wider(names_from=task, values_from=res) %>%
  kable
```

| sample | read | sorting + compressing + indexing | read mapping | coverage track |
|:---|---:|:---|:---|:---|
| Breast epithelium | 193.6 | 0.3 cpu.h (1 Gb) | 8.9 cpu.h (54 Gb) | 3 cpu.h (109 Gb) |
| Gastrocnemius medialis | 98.8 | 0.3 cpu.h (1 Gb) | 4.8 cpu.h (54 Gb) | 2.6 cpu.h (99 Gb) |
| Gastroesophageal sphincter | 168.5 | 0.2 cpu.h (1 Gb) | 7.3 cpu.h (54 Gb) | 3 cpu.h (108 Gb) |
| Peyer’s patch | 145.3 | 0.2 cpu.h (1 Gb) | 8 cpu.h (54 Gb) | 3 cpu.h (104 Gb) |
| Sigmoid colon | 173.5 | 0.3 cpu.h (1 Gb) | 8.2 cpu.h (54 Gb) | 3 cpu.h (106 Gb) |
| Spleen | 157.2 | 0.2 cpu.h (1 Gb) | 7.6 cpu.h (54 Gb) | 3 cpu.h (104 Gb) |
| Thyroid gland | 91.4 | 0.1 cpu.h (1 Gb) | 4.6 cpu.h (54 Gb) | 2.5 cpu.h (94 Gb) |

## Summary of the coverage tracks

Read summaries:

``` r
cs.df = lapply(list.files('results', 'cov.sum.tsv', recursive=TRUE), function(fn){
  read.table(paste0('results/', fn), as.is=TRUE, header=TRUE, sep='\t') %>%
    mutate(sample=gsub('.*/(.*).cov.sum.tsv', '\\1', fn))
}) %>% bind_rows
head(cs.df)
```

    ##   coverage_bin n_node n_bp      n            sample
    ## 1            1      1    4 135115 breast_epithelium
    ## 2            1      3   36   1854 breast_epithelium
    ## 3            2     10  231    128 breast_epithelium
    ## 4            3      1    1 438436 breast_epithelium
    ## 5            5      1   25  92027 breast_epithelium
    ## 6            2     11  245    188 breast_epithelium

Summarize the coverage track for each sample:

``` r
min.coverage = 10
cs.s = cs.df %>% filter(coverage_bin>=min.coverage) %>% 
  group_by(sample) %>%
  summarize(paths=sum(n),
            mean_bases=sum(n*n_bp)/paths,
            mean_nodes=sum(n*n_node)/paths,
            n_mt2nodes=sum(n*n_node>2),
            prop_mt2nodes=n_mt2nodes/paths)

cs.s %>% 
  mutate(mt2nodes=paste0(format(n_mt2nodes, big.mark=','),
                         ' (', round(100*prop_mt2nodes, 1), '%)'),
         mean_bases=round(mean_bases, 2),
         mean_nodes=round(mean_nodes, 2),
         sample=factor(sample, samp.levs, samp.labs)) %>%
  select(-n_mt2nodes, -prop_mt2nodes) %>%
  arrange(sample) %>% 
  kable(format.args=list(big.mark=','))
```

| sample                     |   paths | mean_bases | mean_nodes | mt2nodes       |
|:---------------------------|--------:|-----------:|-----------:|:---------------|
| Breast epithelium          | 570,155 |     109.80 |       2.68 | 65,095 (11.4%) |
| Gastrocnemius medialis     | 342,830 |      94.47 |       2.43 | 53,595 (15.6%) |
| Gastroesophageal sphincter | 555,618 |     115.69 |       2.73 | 72,407 (13%)   |
| Peyer’s patch              | 270,094 |      97.88 |       2.62 | 43,591 (16.1%) |
| Sigmoid colon              | 678,380 |     115.10 |       2.69 | 82,906 (12.2%) |
| Spleen                     | 531,910 |     104.97 |       2.66 | 67,153 (12.6%) |
| Thyroid gland              | 377,157 |      95.63 |       2.41 | 56,441 (15%)   |

Average across samples:

``` r
cs.s %>% select(-sample) %>% summarize_all(mean) %>% kable
```

|    paths | mean_bases | mean_nodes | n_mt2nodes | prop_mt2nodes |
|---------:|-----------:|-----------:|-----------:|--------------:|
| 475163.4 |   104.7908 |   2.601868 |   63026.86 |     0.1371887 |
