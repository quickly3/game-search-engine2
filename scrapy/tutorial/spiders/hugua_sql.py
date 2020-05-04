# -*- coding:UTF-8 -*-
#
from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from operator import itemgetter
from itertools import groupby
import scrapy
import os
import re
from string import Template

from dotenv import load_dotenv
from pathlib import Path

env_path = Path('..')/'.env'
load_dotenv(dotenv_path=env_path)

DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# settings.py


es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")
es = Elasticsearch(http_auth=(es_user, es_pwd))
es_logger.setLevel(50)


engine = create_engine("mysql+pymysql://"+DB_USERNAME+":"+DB_PASSWORD +
                       "@localhost/"+DB_DATABASE+"?charset=utf8", encoding='utf-8', echo=False)

Base = declarative_base()
Session_class = sessionmaker(bind=engine)
Session = Session_class()


class Huagua(Base):
    __tablename__ = 'hugua'
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    state = Column(Integer)


def cont_filter(x):
    return x.replace("、", ".").replace("\n", "").strip(" ") != ""


def distinct(items):
    key = itemgetter('link')
    items = sorted(items, key=key)
    return [next(v) for _, v in groupby(items, key=key)]


class AliSpider(scrapy.Spider):
    # 593
    name = "hugua_sql"
    source = "hugua"
    tag = ""

    fanjuList = []
    domain = "http://www.hugua.cc"
    handle_httpstatus_all = True

    def __init__(self,seed=None,*args, **kwargs):
        super(AliSpider, self).__init__(*args, **kwargs)
        self.seed=seed

    def start_requests(self):
        return self.next_request()

    def next_request(self):
        records = self.getRecord()
        if records != None:
            for record in records:
                yield scrapy.Request(url=record.url, callback=lambda response, re=record: self.parse(response, re), meta={'handle_httpstatus_all': True})       

    def getRecord(self):
        try:
            if self.seed == None:
                record = Session.query(Huagua).filter(Huagua.state == 0).order_by(Huagua.id).limit(1).all()
            else:
                sql_t = Template("""SELECT * FROM hugua
                    WHERE state = 0
                    and id % 10 = ${seed}
                    ORDER BY id 
                    LIMIT 1""")

                sql_query = sql_t.substitute(seed=self.seed)

                cursor = Session.execute(sql_query)
                record = cursor.fetchall()

            if len(record) == 0:
                return None
            return record
        except BaseException:
            return None

    def analysisPage(self, resp, record):

        bulk = []

        title = resp.xpath('//*[@id="detail-focus"]/div[2]/h2/text()').get();
        image = resp.xpath('//*[@id="detail-focus"]/div[1]/img/@src').get();
        lang = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dl[4]/dd/span/text()').get()
        type = resp.xpath('//*[@id="detail-focus"]/div[2]/dl/dl[3]/dd/a/text()').get()

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

    def parse(self, resp, record):

        if resp.status != 200:
            self.updateRecord(record.id, 2)
            return self.next_request();
        else:

            self.analysisPage(resp, record)
            self.updateRecord(record.id, 1)
            return self.next_request()

    def updateRecord(self, id, state):
        update_obj = {
            Huagua.state: state,
        }

        Session.query(Huagua).filter(
            Huagua.id == id).update(update_obj)
        Session.commit()
