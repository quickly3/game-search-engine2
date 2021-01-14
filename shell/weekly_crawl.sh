#!/bin/sh
export PATH=$PATH:/usr/local/bin   

cd /home/ubuntu/www/ng-blog/scrapy
nohup python3 -m scrapy crawl elastic_cn >> /home/ubuntu/www/ng-blog/storage/logs/elastic_cn.log 2>&1

cd /home/ubuntu/www/ng-blog
nohup sudo php artisan EsClear elastic_cn >> /home/ubuntu/www/ng-blog/storage/logs/elastic_cn.log 2>&1
