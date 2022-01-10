# -*- coding:UTF-8 -*-
#
#

import scrapy
import os
import json
import datetime
import time

# settings.py
from dotenv import load_dotenv
from pathlib import Path

from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger


env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
log_level = os.getenv("ES_LOG")

es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


def clearHighLight(string):
    string = string.replace("<em>", "")
    string = string.replace("</em>", "")
    return string


class AliSpider(scrapy.Spider):
    # 593
    name = "cnblogs_daily"

    tagId = {
        "后端开发": {
            "cid": "2"
        },
        ".NET技术": {
            "cid": "108698"
        },
        "Java": {
            "cid": "106876"
        },
        "Python": {
            "cid": "108696"
        },
        "Go": {
            "cid": "108748"
        },
        "PHP": {
            "cid": "106882"
        },
        "C++": {
            "cid": "106880"
        },
        "Ruby": {
            "cid": "106894"
        },
        "Swift": {
            "cid": "108751"
        },
        "C语言": {
            "cid": "108735"
        },
        "Erlang": {
            "cid": "108746"
        },
        "Delphi": {
            "cid": "106877"
        },
        "Scala": {
            "cid": "108752"
        },
        "R语言": {
            "cid": "108753"
        },
        "Verilog": {
            "cid": "108742"
        },
        "Dart": {
            "cid": "108765"
        },
        "其他语言": {
            "cid": "108754",
            "extra_tag": "后端开发"
        },

        "架构设计": {
            "cid": "106892"
        },
        "所有随笔": {
            "cid": "0"
        },
        "设计模式": {
            "cid": "106884"
        },
        "领域驱动设计": {
            "cid": "108750",
            "extra_tag": "软件设计"
        },
        "Html/Css": {
            "cid": "106883"
        },
        "JavaScript": {
            "cid": "106893"
        },
        "jQuery": {
            "cid": "108731"
        },
        "HTML5": {
            "cid": "108737"
        },
        "Angular": {
            "cid": "108770"
        },
        "React": {
            "cid": "108771"
        },
        "Vue": {
            "cid": "108772",
            "extra_tag": "前端开发"
        },

        "BPM": {
            "cid": "108761"
        },
        "SharePoint": {
            "cid": "78111"
        },
        "GIS技术": {
            "cid": "50349"
        },
        "SAP": {
            "cid": "106878"
        },
        "Oracle ERP": {
            "cid": "108732"
        },
        "Dynamics": {
            "cid": "108734"
        },
        "信息安全": {
            "cid": "108749",
            "extra_tag": "企业信息化"
        },

        "Android开发": {
            "cid": "108706"
        },
        "iOS开发": {
            "cid": "108707"
        },
        "Flutter": {
            "cid": "108768"
        },
        "鸿蒙": {
            "cid": "108769"
        },
        "其他手机开发": {
            "cid": "106886",
            "extra_tag": "移动端开发"
        },
        "敏捷开发": {
            "cid": "108710"
        },
        "项目与团队管理": {
            "cid": "106891"
        },
        "软件工程其他": {
            "cid": "106889",
            "extra_tag": "软件工程"
        },
        "SQL Server": {
            "cid": "108713"
        },
        "Oracle": {
            "cid": "108714"
        },
        "MySQL": {
            "cid": "108715"
        },
        "PostgreSQL": {
            "cid": "108767"
        },
        "NoSQL": {
            "cid": "108743"
        },
        "大数据": {
            "cid": "108756"
        },
        "其他数据库": {
            "cid": "106881",
            "extra_tag": "数据库"
        },
        "Windows": {
            "cid": "108721"
        },
        "Windows Server": {
            "cid": "108725"
        },
        "Linux": {
            "cid": "108726"
        },
        "macOS": {
            "cid": "108755"
        },
        "嵌入式": {
            "cid": "108757",
            "extra_tag": "操作系统"
        },
        "非技术区": {
            "cid": "807"
        },
        "软件测试": {
            "cid": "106879"
        },
        "代码与软件发布": {
            "cid": "33909"
        },
        "计算机图形学": {
            "cid": "106885"
        },
        "游戏开发": {
            "cid": "108759"
        },
        "程序人生": {
            "cid": "106888"
        },
        "求职面试": {
            "cid": "106890"
        },
        "读书区": {
            "cid": "5079"
        },
        "转载区": {
            "cid": "4347"
        },
        "翻译区": {
            "cid": "106875"
        },
        "开源研究": {
            "cid": "108722"
        },
        "云计算": {
            "cid": "108740"
        },
        "算法与数据结构": {
            "cid": "108741"
        },
        "人工智能": {
            "cid": "108762"
        },
        "区块链": {
            "cid": "108764"
        },
        "网络安全": {
            "cid": "108766"
        },
        "其他技术区": {
            "cid": "7734",
            "extra_tag": "其他分类"
        }
    }

    tag = "python"
    source = "cnblogs"
    tag_index = 0

    pager_url = "https://www.cnblogs.com/AggSite/AggSitePostList"

    page = 1
    pageSize = 20

    headers = {
        "Authority": "www.cnblogs.com",
        "Accept": "text/plain, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Origin": "https://www.cnblogs.com",
        "X-requested-with": "XMLHttpRequest",
        "Referer": "https://www.cnblogs.com/cate/python/",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 ,Safari/537.36"
    }

    def start_requests(self):
        self.tag_arr = []
        for tag in self.tagId:
            self.tag_arr.append(tag)

        self.tag = self.tag_arr.pop()
        self.cateId = self.tagId[self.tag]['cid']
        self.extra_tag = self.tagId[self.tag]['extra_tag']

        formdata = self.get_formdata()


        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        self.start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        self.end_time = self.start_time + 86400


        temp = json.dumps(formdata)

        url = self.pager_url
        yield scrapy.FormRequest(url=url, body=temp, method="POST", headers=self.headers)

    def next_request(self, next_tag=False):

        if next_tag == True:
            if len(self.tag_arr) == 0:
                self.crawler.engine.close_spider(self, '关闭爬虫')
            else:
                self.page = 0
                self.tag = self.tag_arr.pop()
                self.cateId = self.tagId[self.tag]['cid']

                if 'extra_tag' in self.tagId[self.tag]:
                    self.extra_tag = self.tagId[self.tag]['extra_tag']


        self.page = self.page + 1
        formdata = self.get_formdata()

        temp = json.dumps(formdata)

        url = self.pager_url
        return scrapy.FormRequest(url=url, body=temp, method="POST", headers=self.headers)

    def get_formdata(self):
        return {"CategoryType": "SiteCategory", "ParentCategoryId": 2, "CategoryId": self.cateId, "PageIndex": self.page, "TotalPostCount": 4000, "ItemListActionName": "AggSitePostList"}

    def parse(self, response):

        items = response.xpath('//*[@class="post-item-body"]')
        bulk = []
        next_tag = False

        if len(items) > 0:
            for item in items:
                doc = {}

                title = item.xpath(
                    '*/a[@class="post-item-title"]/text()').get()
                url = item.xpath('*/a[@class="post-item-title"]/@href').get()

                desps = item.xpath(
                    '*/p[@class="post-item-summary"]/text()').getall()
                desp = "".join(desps)
                desp = desp.strip()

                author = item.xpath(
                    '*/a[@class="post-item-author"]/span/text()').get()

                created_at = item.xpath(
                    '*/span[@class="post-meta-item"]/span/text()').getall()

                if len(created_at) > 0:
                    created_at = created_at[0]
                    date_time_obj = datetime.datetime.strptime(
                        created_at, '%Y-%m-%d %H:%M')

                    doc['created_at'] = date_time_obj.strftime(
                        "%Y-%m-%dT%H:%M:%SZ")
                    doc['created_year'] = date_time_obj.strftime("%Y")

                    date_time_obj = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M')

                    doc['created_at'] = date_time_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
                    doc['created_year'] = date_time_obj.strftime("%Y")

                ts = date_time_obj.timestamp();

                if ts < self.start_time :
                    next_tag = True;
                    # print("too old")
                    continue;

                if ts > self.end_time :
                    # print("too new")
                    continue;


                doc['title'] = title
                doc['url'] = url

                doc['tag'] = [self.tag,self.extra_tag]
                doc['summary'] = desp
                doc['source'] = self.source
                doc['source_score'] = 0

                doc['author'] = author

                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)

        else:
            print("Next")
            next_tag = True

        if len(bulk) > 0:
            es.bulk(index="article", body=bulk)

        if next_tag:
            yield self.next_request(next_tag)
