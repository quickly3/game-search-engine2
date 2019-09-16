# Game Search Engine

> 这是一个自动收集游戏信息并提供搜索引擎服务的项目

### 网站地址

<http://www.zhouhongbin.com>

### 主要开源技术

> 后端框架 Laravel 5.8  
> 前端框架 Angular 8
> 爬虫框架 Scrapy 1.4  
> 搜索引擎 ElasticSearch 6.5  
> 关系数据库 mysql 5.7

### 爬虫数据源

> 游侠网

### 安装部署

> npm install  
> composer install  
> php artisan key:generate  
> 前端开发 监听模式 npm run watch  
> 部署模式 npm run prod

### 爬虫命令

> 爬虫代码在 scrapy 目录下

游侠网

> scrapy crawl ali  
> scrapy crawl ali2

Elasticsearch 日报

> scrapy crawl escn  
> scrapy crawl escn2

Nba 数据

> scrapy crawl nba_player

B 站弹幕

> scrapy crawl fanju
> scrapy crawl episode
> scrapy crawl danmu

scrapy crawl episode -a ssid=_
scrapy crawl danmu -a ssid=_

nohup scrapy crawl danmu > d.log &
nohup scrapy crawl danmu > d.log 2>&1 &

### 数据挖掘

> ???有么

### 全量数据同步

> php artisan elastic:migrate "App\Models\GameModel" games_20190916
> php artisan elastic:migrate "App\Models\EscnModel" escn_20190916

### 增量数据同步

> sudo php artisan MysqlToEs  
> sudo php artisan EscnToEs

### 更多数据源和功能

> 挤时间中...

### 理论模型

> 喵喵喵？
