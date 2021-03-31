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
    name = "gl"

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

    def start_requests(self):
        prefix = 'https://www.google.com/search?';
        
        self.companies = self.companies + list(map(lambda x: x+" linkedin",self.companies))
        for keyword in self.companies:
            urlencodeKeyword = urlencode({'q':keyword});
            url = prefix+urlencodeKeyword
            yield scrapy.FormRequest(url=url, method="GET",callback=lambda response, keyword=keyword: self.parse(response, keyword))

    def parse(self, response, keyword):
        print(response)

                    


        