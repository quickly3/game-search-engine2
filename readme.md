# Game Search Engine

> 这是一个自动收集游戏信息并提供搜索引擎服务的项目

技术博客类爬虫、搜索引擎：只爬取特定一些分类的博客的 title，link，summary,createdate，存到 elasticsearch 中，用来做类似订阅功能，分析最近热点博客，及基于 Elasticsearch 开发跨站真实搜索引擎的各种实际功能。

游侠网免费游戏搜索引擎：

其他各种爬虫：

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