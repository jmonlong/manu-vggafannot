suppressPackageStartupMessages(library(dplyr))
library(knitr)

bm.df = lapply(list.files('benchmark'), function(fpath){
  df = read.table(paste0('benchmark/', fpath), as.is=TRUE, sep='\t', header=TRUE)
  df$task = gsub('.tsv', '', fpath)
  df %>% select(task, max_rss, mean_load, cpu_time, h.m.s)
}) %>% bind_rows

bm.df %>% arrange(cpu_time) %>% kable(format.args=list(big.mark=','))
