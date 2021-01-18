#!/bin/sh
export PATH=$PATH:/usr/local/bin   

cd /home/ubuntu/www/ng-blog/scrapy
nohup python3 -m scrapy crawl escn_new >> /home/ubuntu/www/ng-blog/storage/logs/escn_new.log 2>&1
nohup python3 -m scrapy crawl jianshu_daily >> /home/ubuntu/www/ng-blog/storage/logs/jianshu_daily.log 2>&1
nohup python3 -m scrapy crawl infoq_daily >> /home/ubuntu/www/ng-blog/storage/logs/infoq_daily.log 2>&1
nohup python3 -m scrapy crawl sf_daily >> /home/ubuntu/www/ng-blog/storage/logs/sf_daily.log 2>&1
nohup python3 -m scrapy crawl juejin_daily >> /home/ubuntu/www/ng-blog/storage/logs/juejin_daily.log 2>&1
nohup python3 -m scrapy crawl cb_daily >> /home/ubuntu/www/ng-blog/storage/logs/cb_daily.log 2>&1



cd /home/ubuntu/www/ng-blog
nohup sudo php artisan EsClearLast >> /home/ubuntu/www/ng-blog/storage/logs/EsClearLast.log 2>&1
