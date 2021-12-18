#!/bin/sh
export PATH=$PATH:/usr/local/bin

cd /home/ubuntu/www/ng-blog/scrapy/juejin

nohup python3 -m juejin_author_crawl >> juejin_author_crawl.log 2>&1 &
