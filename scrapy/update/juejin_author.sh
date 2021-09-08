#!/bin/sh
export PATH=$PATH:/usr/local/bin

cd /home/ubuntu/www/ng-blog/scrapy/update

nohup python3 -m juejin_author_crawl.py >> juejin_author_crawl.log 2>&1
