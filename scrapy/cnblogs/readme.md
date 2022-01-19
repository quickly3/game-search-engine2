nohup python3 crawl_by_author.py  >> crawl_by_author.txt 2>&1 &

nohup scrapy crawl infoq_t2 >> crawl.log 2>&1 &

tail -f crawl.log

scrapy crawl oschina_news