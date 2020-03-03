# 数据采集之爬虫篇

```
主要使用基于Python scrapy
```

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

```
关于实例：
大多数实例的设计目的，是为练习在平时设自用爬虫时常用到的功能点，以及为Elasticsearch项目提供实操数据，因此会有多余的业务代码，请根据实际情况自行修改。
```

```
Tips:
最近把存储用Elasticsearch 从6.7 升级到了7.6，部分爬虫的代码还未更新，会产生写入bug，后续会把爬虫代码进行相应升级
```

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

```
技术博客类爬虫：只爬取特定一些分类的博客的title，link，summary,createdate，存到elasticsearch中，用来做类似订阅功能，分析最近热点博客，及基于Elasticsearch 开发跨站真实搜索引擎的各种实际功能。
```

其他类爬虫：

- [B 站弹幕](#B站弹幕)

- [游侠网游戏](#游侠网游戏)

- [游侠网福利图](#游侠网福利图)

- [胡瓜影院](#胡瓜影院)

#### Elasticsearch 中文社区日报

#### 简书

#### Segmentfault 思否

#### CSDN

#### 博客园 cnblog

#### 掘金

#### 开源中国

#### infoq

#### B 站弹幕

`关键词: Json接口爬取，图片下载，自动生成csv,打包zip，Elasticsearch中文分词器`

```
说明：
弹幕番剧层级关系：fanju(番剧列表) -> episode(剧集列表) -> danmu(每集弹幕)
每层数据都挺多，因此分为三个爬虫，按照顺序执行
```

爬虫源码：

fanju：

[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/fanju.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/fanju.py)

episode:

[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/episode.py
](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/episode.py)

danmu:
[https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/danmu.py](https://github.com/quickly3/game-search-engine2/blob/master/scrapy/tutorial/spiders/danmu.py)

#### 游侠网游戏

#### 游侠网福利图

#### 胡瓜影院
