scrapy crawl juejin_tag

nohup python3 -m juejin_tag_crawl >> juejin_tags_nohup.log 2>&1 &

python juejin_author_output
nohup python3 -m juejin_author_crawl >> juejin_author_crawl.log 2>&1 &

scrapy juejin_authors_crawl
