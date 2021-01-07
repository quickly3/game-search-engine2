#!/bin/sh
export PATH=$PATH:/usr/local/bin   

cd /home/ubuntu/www/ng-blog/scrapy
nohup python3 -m scrapy crawl escn_new >> /home/ubuntu/www/ng-blog/storage/logs/escn_new.log 2>&1
nohup python3 -m scrapy crawl jianshu_daily >> /home/ubuntu/www/ng-blog/storage/logs/jianshu_daily.log 2>&1
nohup python3 -m scrapy crawl infoq_daily >> /home/ubuntu/www/ng-blog/storage/logs/jianshu_daily.log 2>&1

cd /home/ubuntu/www/ng-blog
nohup sudo php artisan EsClear jianshu >> /home/ubuntu/www/ng-blog/storage/logs/JianshuClear.log 2>&1
nohup sudo php artisan EsClear infoq >> /home/ubuntu/www/ng-blog/storage/logs/InfoqClear.log 2>&1
