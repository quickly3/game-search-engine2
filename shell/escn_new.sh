#!/bin/sh
export PATH=$PATH:/usr/local/bin   

cd /home/ubuntu/www/ng-blog/scrapy
nohup python3 -m scrapy crawl escn_new >> scrapy.log 2>&1
nohup python3 -m scrapy crawl jianshu_daily >> scrapy.log 2>&1