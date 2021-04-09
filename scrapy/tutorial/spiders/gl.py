# -*- coding:UTF-8 -*-
#
#
import scrapy
import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode
import json
import sys

class AliSpider(scrapy.Spider):
    # 593
    name = "gl"

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
    input_file = 'companies.csv'
    output_file = 'linked_companies.csv'

    def start_requests(self):

        file = open(self.input_file, 'r')
        text_lines = file.readlines()

        prefix = 'https://www.google.com/search?';
        
        # self.companies = self.companies + list(map(lambda x: x+" linkedin",self.companies))

        for keyword in text_lines:
            keyword = 'site:www.linkedin.com '+keyword.replace("\"","").replace("\n","")
            
            urlencodeKeyword = urlencode({'q':keyword});
            url = prefix+urlencodeKeyword
            print(url)

            yield scrapy.FormRequest(url=url, method="GET",callback=lambda response, keyword=keyword: self.parse(response, keyword))

    # def exactlyMatch(self,item):
    #     company = {}
    #     company['type'] = 'exactly'
    #     company['name'] = item.xpath('div/div[1]/span[1]/h3/div/text()').get();
    #     intro = item.xpath('div/div[1]/span[2]/div/text()').get();
    #     company['intro'] = intro if intro else ''

    #     infos = item.xpath('div/div[3]/div/a');
    #     for info in infos:
    #         key = info.xpath('div[2]/text()').get();
    #         key = key.lower()
    #         href = info.xpath('@href').get();

    #         links = self.redirectLinkParse(href)
            
    #         company[key] = links['href'];
    #         company[google_redirect] = links['google_redirect'];


    #     intro2 = item.xpath('div/div[4]/div')
    #     if intro2:
    #         for line in intro2:
    #             key = line.xpath('div/span[1]/span/text()').get();
    #             key = key.lower()
    #             value = line.xpath('div/span[2]/span/text()').get();
    #             company[key] = value;
        
    #     return company

    # def redirectLinkParse(self,href):
    #     google_redirect = 'https://www.google.com/'+href;
    #     parsed_url = urlparse.urlparse(href)
    #     params = parse_qs(parsed_url.query)
    #     if params['q']:
    #         href = params['q'][0]
    #     else:
    #         href = google_redirect
        
    #     return {
    #         'href':href,
    #         'google_redirect':google_redirect
    #     }

    # def commonMatch(self,item):
    #     company = {}
    #     company['type'] = 'common';
    #     company['name'] = item.xpath('div/div[1]/a/h3/div/text()').get()
    #     company['source'] = item.xpath('div/div[1]/a/div/text()').get()
    #     company['intro'] = item.xpath('div/div[3]/div/div/div/div/div/text()').get()

    #     href = item.xpath('div/div[1]/a/@href').get()
    #     links = self.redirectLinkParse(href)
    #     company['website'] = links['href']
    #     company['google_redirect'] = links['google_redirect'];
    #     return company

    def parse(self, response, keyword):
        htmlFile = f"/Users/hongbinzhou/Downloads/companies/{keyword}.html"
        # jsonFile = f"/Users/hongbinzhou/Downloads/companies/{keyword}.json"

        f = open(htmlFile, "w")
        f.write(response.text)
        f.close()
        
        items = response.xpath('//*[@id="main"]/div');
        list = []
        for i in range(len(items)):
            if i > 1:
                item = items[i];
                imageMark = item.xpath('div/div[1]/div[1]/span/a/span/span/text()').get();
                exactly = item.xpath('div/div[1]/span[1]/h3/div/text()').get();
                print(exactly)
                # if imageMark == 'Images':
                #     continue;

                # if exactly:
                #     company = self.exactlyMatch(item)
                # else:
                #     company = self.commonMatch(item)

                # list.append(company)
                
        # with open(jsonFile, 'w') as fout:
        #     json.dump(list, fout)
