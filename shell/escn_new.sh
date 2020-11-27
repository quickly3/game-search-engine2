#!/bin/sh
export PATH=$PATH:/usr/local/bin   

cd /home/ubuntu/www/ng-blog/scrapy
nohup python3 -m scrapy crawl escn_new >> scrapy.log 2>&1