# 数据采集之爬虫篇

主要使用基于 Python scrapy

[Scrapy 官网 https://scrapy.org](https://scrapy.org/)

[Scrapy Doc https://docs.scrapy.org/en/latest](https://docs.scrapy.org/en/latest/)

## 学习线

- Scrapy 爬虫对象
- Css / Xpath Selector
- header 伪造
- 网页迭代,轮询
- 中间件
- IP 伪造、代理池
- 分布式
- 反爬虫

### 实例

关于实例：
大多数实例的设计目的，是为练习在平时设自用爬虫时常用到的功能点，以及为 Elasticsearch 项目提供实操数据，因此会有多余的业务代码，请根据实际情况自行修改。

Tips:
最近把存储用 Elasticsearch 从 6.7 升级到了 7.6，部分爬虫的代码还未更新，会产生写入 bug，后续会把爬虫代码进行相应升级

相关 Python 插件列表：

[https://github.com/quickly3/game-search-engine2/blob/master/pip_install](https://github.com/quickly3/game-search-engine2/blob/master/pip_install)

技术博客类爬虫：

- [Elasticsearch 中文社区日报](#Elasticsearch中文社区日报)
- [简书](#简书)
- [Segmentfault 思否](#Segmentfault思否)
- [CSDN](#CSDN)
- [博客园 cnblog](#博客园cnblog)
- [掘金](#掘金)
- [开源中国](#开源中国)
- [infoq](#infoq)

技术博客类爬虫：只爬取特定一些分类的博客的 title，link，summary,createdate，存到 elasticsearch 中，用来做类似订阅功能，分析最近热点博客，及基于 Elasticsearch 开发跨站真实搜索引擎的各种实际功能。

其他类爬虫：

- [B 站弹幕](#B站弹幕)
- [游侠网游戏](#游侠网游戏)
- [游侠网福利图](#游侠网福利图)
- [胡瓜影院](#胡瓜影院)

#### Elasticsearch 中文社区日报

> 关键词:入门级别爬虫,增量爬虫

说明： 双层结构，日报列表 -> 日报内文章列表 ,自动迭代第二层爬虫，并直接写入 es

命令：  
`scrapy crawl escn_new`

爬虫源码:  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/escn_new.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/escn_new.py)

es mapping:  
[https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping](https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping)

#### 简书

> 关键词:

说明：
命令:  
`scrapy crawl jianshu2`

爬虫源码：

[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/jianshu1.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/jianshu1.py)

[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/jianshu2.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/jianshu2.py)

es mapping:  
[https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping](https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping)

#### Segmentfault 思否

> 关键词:

说明：

命令：  
`scrapy crawl sf`

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/sf.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/sf.py)

es mapping:  
[https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping](https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping)

#### CSDN

> 关键词:

说明：

命令：  
`scrapy crawl csdn`

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/csdn.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/csdn.py)

es mapping:  
[https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping](https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping)

#### 博客园 cnblog

> 关键词:

说明：

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/cnblogs.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/cnblogs.py)

es mapping:  
[https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping](https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping)

#### 掘金

> 关键词:

命令：  
`scrapy crawl juejin`

说明：

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/juejin.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/juejin.py)

es mapping:  
[https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping](https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping)

#### 开源中国

> 关键词:

命令：  
`scrapy crawl oschina`

说明：

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/oschina.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/oschina.py)

es mapping:  
[https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping](https://github.com/quickly3/game-search-engine2/blob/master/database/mapping/article.mapping)

#### infoq

> 关键词:IP 禁止访问，反爬虫

说明：
直接爬取得对象是搜索引擎，服务器端防爬，根据 web 服务器端 IP 记录，计算大量请求的 IP，禁止 IP 访问

命令：  
`scrapy crawl infoq`

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/infoq.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/infoq.py)

#### B 站弹幕

> 关键词: Json 接口爬取，图片下载，自动生成 csv,打包 zip

说明：
弹幕番剧层级关系：fanju(番剧列表) -> episode(剧集列表) -> danmu(每集弹幕)
每层数据都挺多，因此分为三个爬虫，按照顺序执行

爬虫源码：

fanju：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/fanju.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/fanju.py)

episode:  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/episode.py
](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/episode.py)

danmu:  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/danmu.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/danmu.py)

#### 游侠网游戏

> 关键词:原生 html，与多类型的 elastchsearch mapping

说明： 使用原生图源，避免空间消耗。使用 mysql 作为存储中间层，使用 laravel scount 自动同步到 es.
双层爬虫

爬虫源码：

[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/ali_spider.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/ali_spider.py)

[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/ali2_spider.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/ali2_spider.py)

#### 游侠网搞笑图

> 关键词:gif 图片下载要用特殊下载中间件

命令：  
`scrapy crawl ali_fuli1`

说明：搞笑图片,动态 gif 与一般图片要用不同的 middleware，占用空间大

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/ali_fuli1.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/ali_fuli1.py)

#### 胡瓜影院

> 关键词:

说明：各种免费网站，没有打包下载链接，需要你一集一集的点，很麻烦。

爬虫源码：  
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/hugua.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/hugua.py)
