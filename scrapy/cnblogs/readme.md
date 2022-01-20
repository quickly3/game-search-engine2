nohup python3 juejin_post_crawl_by_author.py  >> crawl.log 2>&1 &

nohup scrapy crawl ali_dev >> crawl.log 2>&1 &

tail -f crawl.log

scrapy crawl oschina_news