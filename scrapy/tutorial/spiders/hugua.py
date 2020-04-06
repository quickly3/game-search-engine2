# -*- coding:UTF-8 -*-
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


es = Elasticsearch()


def cont_filter(x):
    return x.replace("、", ".").replace("\n", "").strip(" ") != ""


def distinct(items):
    key = itemgetter('link')
    items = sorted(items, key=key)
    return [next(v) for _, v in groupby(items, key=key)]


class AliSpider(scrapy.Spider):
    # 593
    name = "hugua"
    start_urls = [
        'http://www.hugua.cc/dongman/185770/',
    ]

    page_list = []

    source = "escn"
    tag = "elastic"

    def parse(self, response):

        file_path = 'C:\\Users\\Administrator\\Desktop\\tmp\\hugua.txt'

        f = open(file_path, "w")

        url = response.css('.downurl>script::text').get()
        url = url.replace("var GvodUrls5 =", "")
        url = url.replace("echoDown(GvodUrls5,5)", "")
        url = url.replace(";", "")
        url = url.replace("\"", "")

        urls = url.split("###")

        for thunder_url in urls:
            line = thunder_url.split("$")
            if thunder_url != "":
                f.write(line[1]+"\n")

        f.close()
