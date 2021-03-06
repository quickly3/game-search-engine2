# -*- coding:UTF-8 -*-
#
#

import scrapy
import sys
import sqlalchemy
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# settings.py
from dotenv import load_dotenv
from pathlib import Path
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


class Game(Base):
    __tablename__ = 'EsDaily'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    link = Column(String(200))
    state = Column(String(200))


class AliSpider(scrapy.Spider):
    # 593
    name = "escn"
    start_urls = [
        # 'http://down.ali213.net/pcgame/all/0-0-0-0-new-pic-604.html'
        'https://elasticsearch.cn/explore/category-18',
    ]

    def parse(self, response):
        has_dup = False
        for item in response.css('.aw-common-list .aw-item'):

            title_h4 = item.css('.aw-question-content h4')
            title = title_h4.css('a::text').extract_first()
            title = title.strip(" ")

            link = title_h4.css('a::attr(href)').extract_first()

            daily_obj = Game(title=title, link=link, state="init")
            duplicate_record = Session.query(
                Game).filter(Game.link == link).first()

            if duplicate_record == None:
                # if title.find("Elastic日报") > -1 :
                Session.add(daily_obj)
                Session.commit()
            else:
                next_page_a_link = None
                has_dup = True

        if has_dup:
            print("End")
            os._exit(0)

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

        if next_page_a_link is not None:
            yield response.follow(next_page_a_link, callback=self.parse)
