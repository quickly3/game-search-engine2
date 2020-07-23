# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os
import json
import datetime
import time

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from string import Template
from dateutil import parser

# settings.py
from dotenv import load_dotenv
from pathlib import Path
import random
import numpy
import pandas as pd


class AliSpider(scrapy.Spider):
    # 593
    name = "infoq_topic"

    mainUrl = "https://www.infoq.cn/public/v1/topic/getList"

    page = 0
    pageSize = 20
    last_score = 0
    
    topic_list = []

    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "www.infoq.cn",
        "Origin": "https://www.infoq.cn",
        "Pragma": "no-cache",
        "Referer": "https://www.infoq.cn/topics",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 ,Safari/537.36"
    }

    def get_body(self,score=0):
        formdata =  {"size": 12}

        if score != 0 :
            formdata['score'] = int(score)
        return json.dumps(formdata)

    def start_requests(self):
        yield scrapy.FormRequest(url=self.mainUrl,body=self.get_body(self.last_score), method="POST",headers=self.headers)

    def parse(self, response):
        resp = json.loads(response.text)

        if len(resp['data']) == 0:

            df_total = pd.DataFrame(self.topic_list)
            df_total = df_total.drop(["desc"],axis=1)

            df_total.to_csv("infoq.csv",mode='w',index=False,encoding="utf-8-sig");
            os._exit(0)
        


        self.topic_list = self.topic_list+resp['data']


        df = pd.DataFrame(resp['data'])

        self.last_score = df.iloc[-1].score


        # if self.last_score > 0:
        #     df.to_csv("infoq.csv",mode='a',index=False);
        # else:
        #     

        # print(self.get_body(self.last_score))
        yield scrapy.FormRequest(url=self.mainUrl,body=self.get_body(self.last_score), method="POST",headers=self.headers)
