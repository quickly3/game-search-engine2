# -*- coding:UTF-8 -*-
#
#
import scrapy
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import json
import os

class AliSpider(scrapy.Spider):
    # 593
    name = "google"
    companies = []
    

    # companies = [
    #     'InceptionPad',
    #     'Bergen Community College','BoxTone Inc','24 Hour Fitness','2U','3Com Corporation',
    #     '3S Media','522 Productions','A-Town Bar and Grill','Abbott Laboratories/Quintiles Commercial',
    #     'Abercrombie & Fitch','Absolute Software','Abstract','Accents by Design','Accenture',
    #     'Access Funding, LLC','ACE Hardware Corporation','Fortren Funding LLC','Acendre',
    #     'Achieved Solutions','Acquia','Acterna','Actian, Corporation','Actuate (opentext)',
    #     'Acuity Audio Visual','AD PAGES MARKETING','ADF Solutions, Inc','Adobe','Adrian College',
    #     'American University','BaseInfoSec','Adtran','Advance Business Systems',
    #     'Advanced & Emerging Technologies','Advanced Computer Concepts','Advantage Green, Inc',
    #     'Advantech','AECOM, Inc','AEG Worldwide','Aerva, Inc','Aether Systems'
    # ]

    # companies = ['InceptionPad']

    def start_requests(self):
        prefix = 'https://www.google.com/search?';
        
        with open("companies.csv") as fp:
            self.companies = fp.readlines()

        fp.close()


        with open("companies.csv") as fp:
            self.companies = fp.readlines()

        fp.close()
        
        self.file2 = "linked_companies.csv"
        self.file3 = "failed_companies.csv"

        # if os.path.isfile(file2):
        #     os.unlink(file2)

 

        self.companies = list(map(lambda x: x.replace("\n",""),self.companies))

        for keyword in self.companies:
            
            urlencodeKeyword = urlencode({'q':"site:www.linkedin.com "+keyword});
            url = prefix+urlencodeKeyword

            yield scrapy.FormRequest(url=url, method="GET",callback=lambda response, keyword=keyword: self.parse(response, keyword))

    def exactlyMatch(self,item):
        company = {}
        company['type'] = 'exactly'
        company['name'] = item.xpath('div/div[1]/span[1]/h3/div/text()').get();
        intro = item.xpath('div/div[1]/span[2]/div/text()').get();
        company['intro'] = intro if intro else ''

        infos = item.xpath('div/div[3]/div/a');
        for info in infos:
            key = info.xpath('div[2]/text()').get();
            key = key.lower()
            href = info.xpath('@href').get();

            links = self.redirectLinkParse(href)
            
            company[key] = links['href'];
            company[google_redirect] = links['google_redirect'];


        intro2 = item.xpath('div/div[4]/div')
        if intro2:
            for line in intro2:
                key = line.xpath('div/span[1]/span/text()').get();
                key = key.lower()
                value = line.xpath('div/span[2]/span/text()').get();
                company[key] = value;
        
        return company

    def redirectLinkParse(self,href):
        google_redirect = 'https://www.google.com/'+href;
        parsed_url = urlparse.urlparse(href)
        params = parse_qs(parsed_url.query)
        if params['q']:
            href = params['q'][0]
        else:
            href = google_redirect
        
        return {
            'href':href,
            'google_redirect':google_redirect
        }

    def commonMatch(self,item):
        company = {}
        company['type'] = 'common';
        company['name'] = item.xpath('div/div[1]/a/h3/div/text()').get()
        company['source'] = item.xpath('div/div[1]/a/div/text()').get()
        company['intro'] = item.xpath('div/div[3]/div/div/div/div/div/text()').get()

        href = item.xpath('div/div[1]/a/@href').get()
        links = self.redirectLinkParse(href)
        company['website'] = links['href']
        company['google_redirect'] = links['google_redirect'];
        return company

    def parse(self, response, keyword):

        f2 = open(file2, "a+")
        f3 = open(file3, "a+")

        href = response.xpath('//*[@id="main"]/div[3]/div/div[1]/a/@href').get();

        if href :
            linkedin_url = self.redirectLinkParse(href);
            f2.write(linkedin_url['href'])
            
        else:
            f3.write(keyword)
        f2.close()
        f3.close()

        





        