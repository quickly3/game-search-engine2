# -*- coding:UTF-8 -*-
#

import scrapy
import sys
import sqlalchemy
import os
import json
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
from string import Template

from elasticsearch import Elasticsearch

es = Elasticsearch()
# import tuorial.settings as sp_setting


env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# engine = create_engine("mysql+pymysql://"+DB_USERNAME+":"+DB_PASSWORD+"@localhost/Game?charset=utf8", encoding='utf-8', echo=False)
engine = create_engine("mysql+pymysql://"+DB_USERNAME+":"+DB_PASSWORD +
                       "@localhost/"+DB_DATABASE+"?charset=utf8", encoding='utf-8', echo=False)
Base = declarative_base()


Session_class = sessionmaker(bind=engine)
Session = Session_class()


class AliSpider(scrapy.Spider):
    # 593
    name = "jianshu2"

    domain = 'https://www.jianshu.com'
    url_list = []
    slug_end = True

    def __init__(self):
        self.collection = [
            # {
            #     "tag": "python",
            #     "slugs":
            #     ['22f2ca261b85', '0bab91ded569', '8c01bfa7b98a', '0690e20b7e7d', 'aa0b21cceb92',
            #      'a480500350e7', '9bc3ae683403', 'bb233a70a20e', '70eae73cf556', '7847442e0728',
            #      '3e3636c40c41', '813a3b29d5fd', '826a1e944a7d', '3ce88fc43e68', '614849b2a5ad',
            #      '24e1fbfc147f', 'd53dd7115ed7', '80fa19f59623', 'dfcf1390085c', '5da7e0427999',
            #      'b0c93dd63315', '24d9279a3f1c', 'f165d63574d2', '38980843c0f2', 'e073fce5432f',
            #      'f204a5f9aac5', '74c5836708df', '4719b64b55a2', '917335d52a08', '954bbd65c3b3']
            # },
            {"tag": "javascript", "slugs":
             [
                 # 'f489ec955505', 'c261fa3879d6',
                 'f63dac4d430e', 'dfdc2bbd1315', '0020d95b7928',
                 '4652107a7847', '38dd7fc9033a', '7c5a95f65440', '4dcf98759530', 'ceb3f53ef4af',
                 'b1f82bbe226e', '69b548699816', '43ae04575967', '0212550c0db3',
                 'a436e05fdbab', 'a283e6c14728', 'ac55040a370c', '0db8232bfad4', '64b644762cef']
             },
            {"tag": "php", "slugs":
             ['71b2d8a98305', 'aaf0e06c2815', '856b74b17595', '5b1d36fefe6a',
              'f78db71563b2', '9e52ed720de5', '669c6b2f44bb', '9d660047f6ff',
              '5d66e811b785', '5e18f1fc1f22', '1301e3720650', 'a4d42d6c3062', '773f827b6e74',
              '0e47180b3a1b', '0e8750d7864b', 'b2c750cad91f', 'f32713612c98', '27de7c36903c']
             },
            {"tag": "css", "slugs":
             ['cb4ec9ef5cd8', '852dc590037e', '598cf0ac363b',
              '50e4b6d88254', '25344f8530b2', '8a0bfaa833d5', '5c595f4a7ded',
              '9f1c932efec0', '7e17aa5ee3ac', '1b8862c44809', '6ef23d0d1d6d', 'a384a1936a62',
              '7cf8294a3adb', '7ad0b3dff3dd', '461df7c67894', '3859c542864d', 'bfb5f14ca7fe']
             },
            {"tag": "typescript", "slugs":
             ['53a0a0a5e1b8', 'b2141d61de73', 'f5c3e5bfd43a',
              '8c1867b6a06c', 'd8a68c43747b', '5006e98ee09e', '1cfc883e264c', '6d2fb4acf852']
             },
            {"tag": "node", "slugs":
             ['38d96caffb2f', 'cf39e87cab8b', '7fafdc0abb5b',
              'e73e318c7f77', '498ebcfd27ad']
             },
            {"tag": "linux", "slugs":
             ['b343b8cdd32b', '0b39448c4e08', 'd836cb84afac', '8700c004b051',
              '51425dc50685', '9a817d8a67ea',
              '6cea47fbc301', '3e62b8833174', '301b723f5e5a',
              'fe5f5bed05c0', '6bbd3c212892', '29440e0d4c48', '5484c13010a0', '1a2f956c9990',
              '0196b27c16c0', '637e399cf78b', '7065d01f4552',
              '01390ac22fa9', '2e21055ceb0e', '4270ad244f46', '4a00c18e77b0', '05f03d0e12c5']
             },
            {"tag": "postgresql", "slugs":
             ['84076305aae3', '562a559bf53f', 'ef81b0409f8d', '28a77e740f32', '4cdc0977d07d',
              '6473407718d1', '1d3745974f0e', '24209b9729a4', 'da29523dffae', 'f69542bf8bae']
             },
            {"tag": "security", "slugs":
             ['76c341b46a81', '1af0c3b76f18', 'f971e98846c6', '0886ffd76168',
              '9a6e0ecd6fbc', '08b19474c52b', '155bb288c68d', '80ce85bed9ae',
              '5c0074b48b8c', '484ecc3e3904', '59515e7b179f', 'c364487f9ccd',
              '4d55123659b0', 'f0b37b938298', 'f0d5c9062134', '0d4d904198f4']
             },
            {"tag": "game", "slugs":
             ['6aa2d74ce7da', 'f35c2b1a3537', '312b44ca0fb8', 'f42580039b45', '865cc3f81e98',
              'b9392b751190', 'aa7dd3c51341', 'f608fc0fb2fe', 'eaac871d1e9f', '4d8b1b7c72db',
              '330be1f135d7', '568894f7edc8', '9336cf7430c4', '581795eb0ded', '31e94ee29b95',
              '2147a9bed1e4', '9ab7731ded1a', '50c2797cc7bb', '9df4cc39bb0f', '92a9ba26cc72']
             },
            {"tag": "block_chain", "slugs":
             ['b17f09dc2831', '7d24bb81f9aa', '76790723269d', 'a63d65402fd7', '65eb459d50cc',
              'b410c42c3933', '9d18f721ec4c', '560477d092db', '5736d9ed99aa', '1b532ee6f848',
              'bcd47c71d7ae', '170c621cedd6', '6cd41bcbf02c', '469d422e39c9', '4ab034109d67',
              'd71bdc853a07', '244a6ebf7036', '288820bb8c87', '896887bfda0a', 'f727af426b80',
              'bef4e958ecd6', 'e3228635bb55', '8c68d4b2eecf', '50d96105fa84', 'bda8683398f9',
              '18cacfe06803', 'efe74104d4e1', '93efec13d95f', 'e809707a89ec', 'be8ab3c15e7f',
              '94039da75221', '646ba80a2e95', '4eed9eac5ae7', 'da9d54bea1cf', '183d48e70cf1',
              'cd01c6ecc603', '25c37cfb5af6', '8e4dd741cff5', '9de9cccf7fd5', 'db7b1e7b1b32']
             }
        ]

        # slugs = {}
        # for tag in self.collection:
        #     for slug in tag['slugs']:
        #         if slug not in slugs:
        #             slugs[slug] = 1
        #         else:
        #             slugs[slug] += 1

        # print(slugs)

        # for tag in slugs:
        #     if slugs[tag] > 1:
        #         print(tag, slugs[tag])
        # os._exit(0)
        # self.slugs = ['954bbd65c3b3']

        self.url_model = Template(
            "https://www.jianshu.com/c/${slug}?order_by=top&page=${page}")

        self.headers1 = {
            "Accept": "text/html, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
            "x-infinitescroll": "true",
            "x-requested-with": "XMLHttpRequest"
        }

        self.headers2 = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/56.0",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cookie": "JSESSIONID=2D1E55287F8B056E83FD29B114FBA389"
        }

        self._page = 43

        self._coll = self.collection.pop(0)

    def getSlugUrl(self):

        if self.slug_end:

            if len(self._coll['slugs']) == 0:
                if len(self.collection) == 0:
                    self.crawler.engine.close_spider(self, '关闭爬虫')
                else:
                    self._coll = self.collection.pop(0)

            self._slug = self._coll['slugs'].pop(0)
            self.slug_end = False

        self._page = self._page+1
        return self.url_model.substitute(slug=self._slug, page=self._page)

    def start_requests(self):
        url = self.getSlugUrl()
        yield scrapy.Request(url, headers=self.headers1)

    def init_page_crawl(self):
        self.slug_end = True
        self.url_list = []
        self._page = 0

    def parse(self, response):

        objs = response.xpath(
            '//li/div')
        bulk = []

        if len(objs) == 0:
            self.init_page_crawl()

        for obj in objs:
            title = obj.xpath('a/text()').get()
            href = obj.xpath('a/@href').get()
            desc = obj.xpath('p/text()').get()
            author = obj.xpath('div/a/text()').get()

            if title == None:
                continue

            doc = {
                "title": title.strip(),
                "title_text": title.strip(),
                "url": href,
                "summary": desc.strip(),
                "tag": self._coll['tag'],
                "author": author,
                # "created_at": href,
                # "created_year": href,
                "source": "jianshu",
                "stars": 0
            }

            # if href in self.url_list:
            #     self.init_page_crawl()
            #     break

            self.url_list.append(href)

            bulk.append(
                {"index": {"_index": "article", "_type": "article"}})
            bulk.append(doc)

        if len(bulk) > 0:
            es.bulk(index="article", doc_type="article",
                    body=bulk, routing=1)

        # if self._page == 5:
        #     self.init_page_crawl()

        url = self.getSlugUrl()

        if url != False:
            # time.sleep(1)
            yield scrapy.Request(url, headers=self.headers1)
        # urls = response.xpath(
        #     '/html/body/div[1]/div/div[1]/div[2]/ul/li/div/a/@href').getall()
        # print(urls)
