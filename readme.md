# Search Gank

> 这是一个专业的IT类信息搜索引擎

### 主要开源技术
> 后端框架 Laravel 8.x  
> 前端框架 Angular 11.x  
> 爬虫框架 Scrapy 2.4    
> 搜索引擎核心 ElasticSearch 7.x 

### 当前已收录信息网站
> Infq  
> SegmentFault  
> 掘金  
> 博客园  
> 简书  
> CSDN  
> 开源中国  
> Elasticsearch 官方博客  
> Elasticsearch 中文社区精品日报  

其他服务：
游侠网免费游戏搜索

### 网站地址

<http://www.searchgank.com>





### 爬虫数据源

> 游侠网

### 安装部署

> npm install  
> composer install  
> php artisan key:generate  
> 前端开发 监听模式 npm run watch  
> 部署模式 npm run prod

### 爬虫

[爬虫列表](https://github.com/quickly3/game-search-engine2/blob/master/readme/spider.md)

### 数据挖掘

> ???有么

### 全量数据同步

> php artisan elastic:migrate "App\Models\GameModel" games_20200227
> php artisan elastic:migrate "App\Models\EscnModel" escn_20190916

### 增量数据同步

> sudo php artisan MysqlToEs  
> sudo php artisan EscnToEs

### 更多数据源和功能

> 挤时间中...
> 免费 IP 代理池爬虫

### 理论模型

> 喵喵喵？

###

部署初始化 laravel scout
php artisan elastic:create-index "App\EsConfigurator\GameConfigurator"
php artisan elastic:create-index "App\EsConfigurator\EscnConfigurator"


scrapy crawl hugua_sql -a seed=1


nohup python nohup.py >> nohup.log 2>&1 &


pproxy -l http://:8181 -r socks5://127.0.0.1:10000 -vv

0 9 * * * /bin/sh /home/ubuntu/www/ng-blog/shell/daily_crawl.sh  >> /home/ubuntu/www/daily.log 2>&1
0 0 * * 1 /bin/sh /home/ubuntu/www/ng-blog/shell/weekly_crawl.sh  >> /home/ubuntu/www/weekly.log 2>&1


nohup node linked2.js > linked2.log 2>&1 &