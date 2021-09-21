import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import json
import os
import urllib.parse
import re
from csv import writer



class TestSpider(scrapy.Spider):
    name = 'yahoo_org'
    handle_httpstatus_list = [404, 500]
    # list = []

    source = 'juejin'
    api_url = 'https://www.bing.com/search?q=site%3Awww.linkedin.com%2Fcompany+<uriCompanyName>';
    domain_url = 'https://www.bing.com/search?q=site%3Awww.linkedin.com%2Fcompany+"<uriCompanyName>"';

    count = 0
    outPut = 'linked_companies.csv'
    findName = 'ONE COMMUNICATIONS'
    toName = True

    def start_requests(self):
        file = 'unlinked_companies.csv'

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)


            for item in _list:

                if item['name'] == self.findName:
                    self.toName = False;

                if self.toName:
                    self.count+=1
                    print(self.count,"/", self.total)
                    continue;


                url = self.api_url.replace('<uriCompanyName>',urllib.parse.quote(item['name']))
                item['query_type'] = 'name'
                yield scrapy.Request(url=url, callback=lambda response, item=item : self.parse(response, item))

                if item['url'].strip() != '':
                    item2 = item.copy()
                    item2['query_type'] = 'url'
                    domain = urllib.parse.urlparse(item2['url']).path
                    if domain is not None:
                        domain = domain.replace('www.','')
                    else:
                        domain = item2['url']

                    url = self.domain_url.replace('<uriCompanyName>',urllib.parse.quote(domain))
                    valid = True

                    if domain.find('linkedin') > -1:
                        valid = False

                    if domain.find('facebook') > -1:
                        valid = False

                    print('domain', domain)

                    if domain.strip() == '':
                        print('empty domain', item2['url'])

                    if valid:
                        yield scrapy.Request(url=url, callback=lambda response, item=item2 : self.parse(response, item))

    def parse(self, response, item):
        self.count+=1
        print(self.count,"/", self.total)

        item['query_type'] = item['query_type']
        item['linkedin_url'] = ''

        linkedin_url = response.xpath('//*[@id="b_results"]/li[1]/h2/a/@href').get();

        if linkedin_url is None:
            linkedin_url = response.xpath('//*[@id="b_results"]/li[2]/h2/a/@href').get();

        if linkedin_url is not None:
            linkedin_url = re.sub(r'\?.*', '', linkedin_url)
            linkedin_url = re.sub(r'#.*', '', linkedin_url)
            linkedin_url = re.sub(r'\/$', '', linkedin_url)
            linkedin_url = linkedin_url + '/about';
            item['linkedin_url'] = linkedin_url;

        List = [i for i in item.values()]
        with open(self.outPut, 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()



if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
