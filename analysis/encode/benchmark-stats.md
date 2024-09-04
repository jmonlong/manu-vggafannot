
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

| task                 | sample                      |         s | h.m.s   |  max\_rss |  max\_vms |  max\_uss |  max\_pss |   io\_in | io\_out | mean\_load | cpu\_time |
| :------------------- | :-------------------------- | --------: | :------ | --------: | --------: | --------: | --------: | -------: | ------: | ---------: | --------: |
| convert\_gbz\_to\_pg | convert\_gbz\_to\_pg        |  293.4269 | 0:04:53 |  13807.30 |  19176.97 |  13807.35 |  13807.35 |     9.30 |    0.00 |      98.39 |    288.94 |
| index\_gaf           | breast\_epithelium          |   19.8297 | 0:00:19 |      5.33 |     12.61 |      3.49 |      4.59 |     2.15 |    0.00 |      76.41 |     15.40 |
| index\_gaf           | gastrocnemius\_medialis     |   12.0046 | 0:00:12 |      5.39 |     12.61 |      3.37 |      4.61 |     2.15 |    0.00 |      87.41 |     10.66 |
| index\_gaf           | gastroesophageal\_sphincter |   19.1831 | 0:00:19 |      5.34 |     12.61 |      3.61 |      4.64 |     2.15 |    0.00 |      80.00 |     15.59 |
| index\_gaf           | PeyersPatch                 |   16.4179 | 0:00:16 |      5.16 |     12.61 |      3.63 |      4.60 |     2.15 |    0.00 |      89.27 |     14.92 |
| index\_gaf           | sigmoid\_colon              |   17.8259 | 0:00:17 |      5.51 |     12.61 |      3.68 |      4.79 |     2.15 |    0.00 |      85.39 |     15.45 |
| index\_gaf           | spleen                      |   16.5991 | 0:00:16 |      5.48 |     12.61 |      3.82 |      4.82 |     2.15 |    0.00 |      88.52 |     14.93 |
| index\_gaf           | thyroid\_gland              |    8.8583 | 0:00:08 |      5.50 |      9.75 |      3.62 |      4.75 |     2.14 |    0.00 |      77.48 |      7.34 |
| make\_cov            | breast\_epithelium          | 7058.8304 | 1:57:38 | 111059.25 | 205535.99 | 111056.23 | 111057.81 |    16.95 |    0.00 |     156.97 |  11080.25 |
| make\_cov            | gastrocnemius\_medialis     | 5641.5133 | 1:34:01 | 101974.03 | 191648.55 | 101970.81 | 101972.39 |    16.95 |    0.00 |     151.26 |   8533.76 |
| make\_cov            | gastroesophageal\_sphincter | 6378.1794 | 1:46:18 | 109562.08 | 201964.57 | 109558.81 | 109560.38 |    16.86 |    0.00 |     153.77 |   9808.20 |
| make\_cov            | PeyersPatch                 | 7142.4634 | 1:59:02 | 106859.24 | 196052.51 | 106856.24 | 106857.70 |    16.86 |    0.00 |     131.04 |   9360.04 |
| make\_cov            | sigmoid\_colon              | 6731.3965 | 1:52:11 | 106863.62 | 197601.46 | 106860.86 | 106862.40 |    16.86 |    0.00 |     143.71 |   9673.90 |
| make\_cov            | spleen                      | 6751.9411 | 1:52:31 | 107509.87 | 198356.05 | 107506.66 | 107508.23 |  3153.57 |    0.00 |     151.83 |  10251.81 |
| make\_cov            | thyroid\_gland              | 5236.4961 | 1:27:16 |  95876.23 | 185185.02 |  95873.32 |  95874.77 |    16.86 |    0.00 |     155.59 |   8147.74 |
| map\_reads           | breast\_epithelium          | 4251.8955 | 1:10:51 |  55581.25 | 104949.44 |  55587.25 |  55588.14 | 47960.77 |    0.00 |     754.67 |  32088.55 |
| map\_reads           | gastrocnemius\_medialis     | 2462.8905 | 0:41:02 |  55692.81 | 104645.94 |  47401.83 |  51548.60 | 20974.76 |    0.00 |     700.66 |  17257.11 |
| map\_reads           | gastroesophageal\_sphincter | 3436.8709 | 0:57:16 |  55712.97 | 104758.94 |  47419.71 |  51566.42 |  1089.15 |    0.00 |     763.49 |  26240.65 |
| map\_reads           | PeyersPatch                 | 3998.0724 | 1:06:38 |  55761.16 | 105003.94 |  55715.89 |  55716.79 |  2699.95 |    0.00 |     717.50 |  28686.33 |
| map\_reads           | sigmoid\_colon              | 3858.0162 | 1:04:18 |  55612.79 | 105033.94 |  55582.70 |  55583.62 | 11093.99 |    0.00 |     765.08 |  29517.25 |
| map\_reads           | spleen                      | 3707.6335 | 1:01:47 |  55714.13 | 104751.44 |  55719.32 |  55720.22 | 25438.74 |    0.00 |     735.76 |  27279.73 |
| map\_reads           | thyroid\_gland              | 2265.1633 | 0:37:45 |  55569.54 | 104830.94 |  47287.90 |  50052.71 |  4799.28 |    0.00 |     725.23 |  16428.36 |
| sort\_cov\_gaf       | breast\_epithelium          |  537.0280 | 0:08:57 |    908.63 |   1319.36 |    907.84 |    908.99 |     9.68 | 4403.77 |     126.08 |    677.42 |
| sort\_cov\_gaf       | gastrocnemius\_medialis     |  298.5232 | 0:04:58 |    795.61 |   1079.36 |    794.71 |    795.91 |     9.68 | 2499.26 |     121.87 |    364.00 |
| sort\_cov\_gaf       | gastroesophageal\_sphincter |  498.0986 | 0:08:18 |    784.54 |   1079.36 |    783.43 |    784.69 |     9.75 | 4068.68 |     128.77 |    641.70 |
| sort\_cov\_gaf       | PeyersPatch                 |  439.6814 | 0:07:19 |    786.46 |   1079.36 |    785.63 |    786.75 |     9.75 | 3535.80 |     127.81 |    562.25 |
| sort\_cov\_gaf       | sigmoid\_colon              |  731.0507 | 0:12:11 |    788.58 |   1079.36 |    787.51 |    788.74 |     9.68 | 3849.96 |      96.08 |    702.63 |
| sort\_cov\_gaf       | spleen                      |  687.1230 | 0:11:27 |    788.66 |   1079.36 |    787.58 |    788.83 |     9.68 | 3573.86 |      97.88 |    672.72 |
| sort\_cov\_gaf       | thyroid\_gland              |  320.2783 | 0:05:20 |    796.46 |   1079.36 |    795.68 |    796.79 |     9.68 | 1769.43 |      98.70 |    316.36 |

## Number of reads

Computed by the snakemake pipeline

``` r
rc.df = lapply(list.files('results', 'wc', recursive=TRUE), function(fn){
  tibble(sample=gsub('.*/(.*).gaf.wc.txt', '\\1', fn),
         read=scan(paste0('results/', fn), 1, quiet=TRUE))
}) %>% bind_rows
kable(rc.df)
```

| sample                      |      read |
| :-------------------------- | --------: |
| breast\_epithelium          | 193556762 |
| gastrocnemius\_medialis     |  98841242 |
| gastroesophageal\_sphincter | 168481212 |
| PeyersPatch                 | 145258696 |
| sigmoid\_colon              | 173532518 |
| spleen                      | 157220976 |
| thyroid\_gland              |  91374726 |

## Summary table

### Average resources per task

``` r
bm.df %>% group_by(task) %>% summarize(cpu_time=mean(cpu_time),
                                       s=mean(s),
                                       mean_load=mean(mean_load),
                                       max_rss=mean(max_rss)) %>%
  kable(format.args=list(big.mark=','))
```

| task                 |  cpu\_time |           s | mean\_load |     max\_rss |
| :------------------- | ---------: | ----------: | ---------: | -----------: |
| convert\_gbz\_to\_pg |    288.940 |   293.42690 |   98.39000 | 1.380730e+04 |
| index\_gaf           |     13.470 |    15.81694 |   83.49714 | 5.387143e+00 |
| make\_cov            |  9,550.814 | 6,420.11717 |  149.16714 | 1.056720e+05 |
| map\_reads           | 25,356.854 | 3,425.79176 |  737.48429 | 5.566352e+04 |
| sort\_cov\_gaf       |    562.440 |   501.68331 |  113.88429 | 8.069914e+02 |

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

| sample                     |  read | sorting + compressing + indexing | read mapping      | coverage track     |
| :------------------------- | ----: | :------------------------------- | :---------------- | :----------------- |
| Breast epithelium          | 193.6 | 0.2 cpu.h (1 Gb)                 | 8.9 cpu.h (54 Gb) | 3.1 cpu.h (108 Gb) |
| Gastrocnemius medialis     |  98.8 | 0.1 cpu.h (1 Gb)                 | 4.8 cpu.h (54 Gb) | 2.4 cpu.h (100 Gb) |
| Gastroesophageal sphincter | 168.5 | 0.2 cpu.h (1 Gb)                 | 7.3 cpu.h (54 Gb) | 2.7 cpu.h (107 Gb) |
| Peyer’s patch              | 145.3 | 0.2 cpu.h (1 Gb)                 | 8 cpu.h (54 Gb)   | 2.6 cpu.h (104 Gb) |
| Sigmoid colon              | 173.5 | 0.2 cpu.h (1 Gb)                 | 8.2 cpu.h (54 Gb) | 2.7 cpu.h (104 Gb) |
| Spleen                     | 157.2 | 0.2 cpu.h (1 Gb)                 | 7.6 cpu.h (54 Gb) | 2.8 cpu.h (105 Gb) |
| Thyroid gland              |  91.4 | 0.1 cpu.h (1 Gb)                 | 4.6 cpu.h (54 Gb) | 2.3 cpu.h (94 Gb)  |

## Summary of the coverage tracks

``` r
cs.df = lapply(list.files('results', 'cov.sum.tsv', recursive=TRUE), function(fn){
  read.table(paste0('results/', fn), as.is=TRUE, header=TRUE, sep='\t') %>%
    mutate(sample=gsub('.*/(.*).cov.sum.tsv', '\\1', fn))
}) %>% bind_rows
head(cs.df)
```

    ##   coverage_bin n_node n_bp      n            sample
    ## 1            1      1    4 138999 breast_epithelium
    ## 2            1      3   36   2047 breast_epithelium
    ## 3            2     10  231    124 breast_epithelium
    ## 4            3      1    1 421106 breast_epithelium
    ## 5            5      1   25  92398 breast_epithelium
    ## 6            2     11  245    151 breast_epithelium

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

| sample                     |   paths | mean\_bases | mean\_nodes | mt2nodes       |
| :------------------------- | ------: | ----------: | ----------: | :------------- |
| Breast epithelium          | 587,869 |      106.45 |        2.59 | 67,050 (11.4%) |
| Gastrocnemius medialis     | 349,293 |       92.39 |        2.38 | 54,953 (15.7%) |
| Gastroesophageal sphincter | 572,482 |      112.12 |        2.64 | 74,849 (13.1%) |
| Peyer’s patch              | 278,081 |       94.93 |        2.54 | 44,852 (16.1%) |
| Sigmoid colon              | 697,030 |      111.76 |        2.61 | 85,362 (12.2%) |
| Spleen                     | 546,530 |      102.00 |        2.59 | 68,880 (12.6%) |
| Thyroid gland              | 383,558 |       93.70 |        2.36 | 58,042 (15.1%) |

``` r
cs.s %>% select(-sample) %>% summarize_all(mean) %>% kable
```

|    paths | mean\_bases | mean\_nodes | n\_mt2nodes | prop\_mt2nodes |
| -------: | ----------: | ----------: | ----------: | -------------: |
| 487834.7 |    101.9079 |    2.528778 |    64855.43 |      0.1376058 |
