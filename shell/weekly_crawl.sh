#!/bin/sh
export PATH=$PATH:/usr/local/bin   

cd /home/ubuntu/www/ng-blog/scrapy
nohup python3 -m scrapy crawl elastic_cn >> /home/ubuntu/www/ng-blog/storage/logs/elastic_cn.log 2>&1
# nohup python3 -m scrapy crawl csdn >> /home/ubuntu/www/ng-blog/storage/logs/csdn.log 2>&1


cd /home/ubuntu/www/ng-blog
nohup sudo php artisan EsClear elastic >> /home/ubuntu/www/ng-blog/storage/logs/elastic_cn.log 2>&1
# nohup sudo php artisan EsClear csdn >> /home/ubuntu/www/ng-blog/storage/logs/csdn.log 2>&1

