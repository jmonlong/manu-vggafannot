library(dplyr)
library(ggplot2)
library(tidyr)
library(knitr)

nregs = 10
reg_size = c(100, 500, 1000)

df = lapply(reg_size, function(rs){
  read.table(paste0('benchmark.query.', nregs, '.', rs, '.tsv'), header=TRUE, sep='\t') %>%
    mutate(size=rs)
}) %>% bind_rows

df %>% group_by(method, size) %>%
  summarize(s=mean(s)) %>%
  pivot_wider(names_from=method, values_from=s) %>%
  kable

df.r = read.table(paste0('benchmark.query.', nregs, '.100.remote.tsv'), header=TRUE, sep='\t')
df.r = df.r %>% mutate(region=factor(region, levels=unique(region)))

ggplot(df.r, aes(x=region, y=s, color=method)) +
  geom_point() + theme_bw()

df.r %>% group_by(method) %>%
  summarize(s=mean(s)) %>%
  pivot_wider(names_from=method, values_from=s) %>%
  kable

pdf('query.time.test.pdf', 7, 9)
ggplot(df, aes(x=factor(size), y=s, fill=method)) +
  geom_boxplot(position='dodge') + theme_bw() +
  xlab('region size (bp)') + coord_flip() +
  scale_fill_brewer(palette='Set2') + 
  ylab('query time (s)')
dev.off()

