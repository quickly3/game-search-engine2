# -*- coding:UTF-8 -*-
#
#

from elasticsearch import Elasticsearch
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from operator import itemgetter
from itertools import groupby
import scrapy
import sys
import sqlalchemy
import os
import re
import datetime


# settings.py
es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")

es = Elasticsearch(http_auth=(es_user, es_pwd))


def cont_filter(x):
    return x.replace("、", ".").replace("\n", "").strip(" ") != ""


def distinct(items):
    key = itemgetter('link')
    items = sorted(items, key=key)
    return [next(v) for _, v in groupby(items, key=key)]


class AliSpider(scrapy.Spider):
    # 593
    name = "escn_all"
    start_urls = [
        'https://elasticsearch.cn/explore/category-18',
    ]

    page_list = []

    source = "escn"
    tag = "elastic"

    def parse(self, response):
        last_create = None
        res = es.search(index="article", body={"query": {"query_string": {
                        "query": "source:escn"}}, "size": 1, "_source": "created_at", "sort": [{"created_at": {"order": "desc"}}]})
        end_crawl = False
        if len(res['hits']['hits']) > 0:
            last_create = res['hits']['hits'][0]['_source']['created_at']
            last_create = datetime.datetime.strptime(last_create, '%Y-%m-%d')

        for item in response.css('.aw-common-list .aw-item'):

            title_h4 = item.css('.aw-question-content h4')
            title = title_h4.css('a::text').extract_first()
            title = title.replace("\n", "").strip(" ")

            mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", title)
            _date = None
            if mat != None:
                _date = mat.group(0)
                _date = datetime.datetime.strptime(_date, '%Y-%m-%d')

                link = title_h4.css('a::attr(href)').extract_first()

                _item = {
                    "title": title,
                    "link": link
                }

                self.page_list.append(_item)

        next_page_li = response.css('.pagination li:nth-last-child(2)')
        next_page_a_text = next_page_li.css('a::text').extract_first()

        if next_page_a_text == ">":
            next_page_a_link = next_page_li.css(
                'a::attr(href)').extract_first()
        else:

            next_page_li = response.css('.pagination li:nth-last-child(1)')
            next_page_a_text = next_page_li.css('a::text').extract_first()

            if next_page_a_text == ">":
                next_page_a_link = next_page_li.css(
                    'a::attr(href)').extract_first()
            else:
                next_page_a_link = None

        if (next_page_a_link is not None) and (not end_crawl):
            yield response.follow(next_page_a_link, callback=self.parse)
        else:

            if len(self.page_list) > 0:

                self.page_list = distinct(self.page_list)
                item = self.page_list.pop(0)
                yield response.follow(item['link'], callback=self.parse_items)

    def parse_items(self, response):

        title = response.xpath(
            "/html/body/div[3]/div/div/div/div[1]/div[1]/div[1]/h1/text()").get()
        title = title.replace("\n", "").strip(" ")

        date = None
        year = None
        mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", title)
        if mat != None:
            date = mat.group(0)
            mat2 = re.search(r"(\d{4})", date)
            year = mat2.group(0)

        t_pattern = re.compile(r'(?<=第)\d+')
        ver = 0
        vers = re.findall(t_pattern, title)

        if len(vers) > 0:
            ver = int(vers[0])

        conuter = 0

        contents = response.css("#markdown_out::text").extract()
        links = response.css("#markdown_out a::attr(href)").extract()

        contents = list(filter(cont_filter, contents))
        if len(contents) == 0:
            contents = response.xpath(
                '//*[@id="markdown_out"]/p/text()').getall()
            links = response.xpath(
                '//*[@id="markdown_out"]/p/a/@href').getall()

        pattern = re.compile(r'^\d\.')

        bulk = []
        for content in contents:

            content = content.replace("、", ".")
            content = content.replace("\n", "")
            content = content.strip()

            match = re.search(r'^\d\.', content)

            if match is not None:
                content = re.sub(pattern, '', content)
                link = links[conuter]
                conuter += 1
                doc = {}

                doc['title'] = content

                doc['url'] = link
                doc['summary'] = title

                doc['tag'] = self.tag
                doc['source'] = self.source

                if date != None:
                    doc['created_at'] = date
                    doc['created_year'] = year

                doc['stars'] = 0
                bulk.append(
                    {"index": {"_index": "article"}})
                bulk.append(doc)

        if len(bulk) > 0:
            es.bulk(index="article", body=bulk)

        if len(self.page_list) > 0:
            item = self.page_list.pop(0)
            yield response.follow(item['link'], callback=self.parse_items)
