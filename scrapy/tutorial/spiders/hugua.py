# -*- coding:UTF-8 -*-
#
from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

from operator import itemgetter
from itertools import groupby
import scrapy
import os
import re

# settings.py


es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


def cont_filter(x):
    return x.replace("、", ".").replace("\n", "").strip(" ") != ""


def distinct(items):
    key = itemgetter('link')
    items = sorted(items, key=key)
    return [next(v) for _, v in groupby(items, key=key)]


class AliSpider(scrapy.Spider):
    # 593
    name = "hugua"
    source = "hugua"
    tag = ""

    fanjuList = []
    domain = "http://www.hugua.cc"

    def start_requests(self):
        # self.pageType = "list"
        # yield scrapy.Request(url='http://www.hugua.cc/dongman/')

        f_path = '../storage/csv/hugua_dongman_list.txt'
        f = open(f_path, "r")  

        lines = f.readlines()
        self.pageType = "detail"
        self.count = len(lines)
        self.current = 0
        for line in lines:
            yield scrapy.Request(url=str.strip(line))

    def parse(self, resp):

        if self.pageType == "list":

            items = resp.xpath('//*[@id="primary"]/div/div[2]/ul/li')

            if len(items) > 0:
                for item in items:
                    url = item.xpath('h5/a/@href').get()
                    self.fanjuList.append(url)

            next_page = resp.xpath('//*[@id="primary"]/div/div[2]/div[2]/div/a[contains(text(), "下一页")]/@href').getall()

            if len(next_page) > 0:
                self.pageType = "list"
                next_page_url = self.domain + next_page[0]

                # for fanju in self.fanjuList:
                #     yield scrapy.Request(url=self.domain+fanju)
                yield scrapy.Request(url=next_page_url)
            else:
                self.pageType = "detail"

                f_path = 'E:\www\game-search-engine2\storage\csv\hugua_list.txt'
                with open(f_path, 'w') as f:
                    for line in self.fanjuList:
                        f.write(self.domain+line+"\n")

                for fanju in self.fanjuList:
                    yield scrapy.Request(url=self.domain+fanju)

        elif self.pageType == "detail":

            bulk = []

            title = resp.xpath('//*[@id="detail-focus"]/div[2]/h2/text()').get();
            image = resp.xpath('//*[@id="detail-focus"]/div[1]/img/@src').get();
            lang = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dl[4]/dd/span/text()').get()
            type = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dl[3]/dd/a/text()').get()
            status = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dl[3]/dd').xpath('string(.)').get()

            alias = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dd/text()').get()
            actors = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dl[1]/dd').xpath('string(.)').get()

            desc = resp.xpath('//*[@id="detail-intro"]/div[2]/div').xpath('string(.)').get()

            year = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dl[5]/dd[2]/text()').get()

            urlStr = resp.css('.downurl>script::text').get()

            downloadUrls = []
            downloadUrlObjs = []

            if urlStr is not None:

                pattern = re.compile('"(.*)"')
                url = pattern.findall(urlStr)

                if len(url) > 0:
                    url = url[0]
                    downloadUrls = url.split("###")

            for downloadUrl in downloadUrls:
                objArr = downloadUrl.split("$")

                if objArr[0].strip() != "":
                    m = re.findall("\d+", objArr[0])
                    
                    if len(m) > 0:
                        m = int(m[0])
                    else:
                        m = 1
                    
                    obj = {
                        'episode': m,
                        'url': objArr[1]
                    }
                    downloadUrlObjs.append(obj)

            playUrls = []
            playItems = resp.xpath('/html/body/div[2]/div[6]/div[2]/div/p/a')

            if len(playItems) > 0:

                for playItem in playItems: 
                    _episode = playItem.xpath('text()').get()
                    _url = playItem.xpath('@href').get()

                    m = re.findall("\d+", _episode)

                    if len(m) > 0 :
                        m = int(m[0])
                    else:
                        m = 1

                    playUrls.append({
                        'episode': m,
                        'url': self.domain + _url
                    })

            doc = {}
            doc['source'] = self.source

            title = title.replace("迅雷下载", "")
            doc['title'] = title
            doc['image'] = image
            doc['lang'] = lang

            desc_end = desc.find("胡瓜")
            if desc_end > 0:
                desc = desc[:desc_end]

            del_end2 = desc.find("主要讲述的是")

            if del_end2 > 0:
                desc = desc[del_end2+6:]

            doc['desc'] = str.strip(desc)
            doc['status'] = status
        
            doc['orgUrl'] = resp.request.url
            doc['type'] = type
            doc['year'] = year
            doc['downloadUrls'] = downloadUrlObjs
            doc['playUrls'] = playUrls

            if alias is not None:
                doc['alias'] = alias
            
            if str.strip(actors) != "未录入":
                actors_arr = actors.split(" ")

                actors_arr = [str.strip(x) for x in actors_arr]
                actors_arr = list(filter(None, actors_arr))
                doc['actors'] = actors_arr
            
            bulk.append(
                {"index": {"_index": "movie"}})
            bulk.append(doc)

            if len(bulk) > 0:
                es.bulk(index="movie", body=bulk)

            self.current += 1
