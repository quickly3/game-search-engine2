# -*- coding:UTF-8 -*-
#
#
import scrapy
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import json

class AliSpider(scrapy.Spider):
    # 593
    name = "linkedin"

    companies = [
        'InceptionPad',
        'Bergen Community College','BoxTone Inc','24 Hour Fitness','2U','3Com Corporation',
        '3S Media','522 Productions','A-Town Bar and Grill','Abbott Laboratories/Quintiles Commercial',
        'Abercrombie & Fitch','Absolute Software','Abstract','Accents by Design','Accenture',
        'Access Funding, LLC','ACE Hardware Corporation','Fortren Funding LLC','Acendre',
        'Achieved Solutions','Acquia','Acterna','Actian, Corporation','Actuate (opentext)',
        'Acuity Audio Visual','AD PAGES MARKETING','ADF Solutions, Inc','Adobe','Adrian College',
        'American University','BaseInfoSec','Adtran','Advance Business Systems',
        'Advanced & Emerging Technologies','Advanced Computer Concepts','Advantage Green, Inc',
        'Advantech','AECOM, Inc','AEG Worldwide','Aerva, Inc','Aether Systems'
    ]

    # companies = ['InceptionPad']

    headers = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'cache-control': 'max-age=0'


    }

    def start_requests(self):
        url = 'https://www.linkedin.com/company/inceptionpad-inc'
        
        cookieFile = '/Users/hongbinzhou/www/ng-blog/scrapy/tutorial/spiders/cookies.json'

        with open(cookieFile) as json_file:
            cookies = json.load(json_file)

        for cookie in cookies:
            print(cookie['name'])
        
        yield scrapy.Request(url,cookies=cookies,headers=self.headers)

    def parse(self, response):
        print(response.text)

                    


        