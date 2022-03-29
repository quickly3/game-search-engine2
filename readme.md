# Search Gank

关注微信公众号，上班摸鱼，获取更多每日互联网新闻~

![即刻资讯](https://mp.weixin.qq.com/mp/qrcode?scene=10000004&size=102&__biz=Mzg2NzUzODY1Nw==&mid=2247483673&idx=1&sn=2c7edf333dada253bfb152646d891b92&send_time= "微信公众号")

# 中文技术互联网态势感知系统

```
通过爬虫主动收集互联网上各大技术博客社区，门户网站的资讯内容，包括但不限于，头条新闻，技术动态，行业趋势，博主博客。
通过手动数据挖掘，机器学习，中文自然语言分析等手段，以时间维度，对收集信息进行整理，归类，存储。
提供搜索引擎，数据聚合，数据可视化，用户内容分析，推荐系统，自动生成聚合后的多媒体内容等服务。
同理该架构技术亦可应用于其它种类互联网信息社区，如观察者网，微博，进行舆论舆情，热点的采集分析，数据增值服务。
```

> 这是一个专业的IT类信息搜索引擎的进化体


### 当前已收录信息网站
> 简书  
> Infq  
> 掘金  
> 博客园  
> CSDN  
> 开源中国  
> SegmentFault  
> Elasticsearch 中文社区
> Elasticsearch 官方博客  
> itpub技术栈
> Datawhale 和鲸社区
> 阿里云开发者社区

### 主要开源技术
> 后端框架 Laravel 8.x  
> 前端框架 Angular 11.x  
> 爬虫框架 Scrapy 2.4    
> 搜索引擎核心 ElasticSearch 7.x 

其他服务：
游侠网免费游戏搜索，下载（已停用）

### 网站地址

<http://www.searchgank.com>



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
> 有了，在做了

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


nohup scrapy crawl oschina >> /home/ubuntu/www/ng-blog/storage/logs/oschina.log 2>&1