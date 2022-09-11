import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.parse import urlparse
from urllib.parse import parse_qs
import os
import re
import sys
import json
import pydash as _
import pprint
from pytz import timezone

pp = pprint.PrettyPrinter(indent=4)

sys.path.append('..')
from es.es_client import EsClient

class TestSpider(scrapy.Spider):
    name = '36kr_all'
    domin = 'https://www.36kr.com'
    source = '36kr'
    current = 0
    total = 0

    def start_requests(self):
        self.es = EsClient()
        start_url = 'https://www.36kr.com/information/web_news/'
        yield scrapy.Request(start_url)

    def parse(self, response):

        pageCallback = re.findall(
            r'(?<="pageCallback":")(.*?)(?=")', str(response.text))
        if len(pageCallback) == 0:
            os._exit(0)

        pageCallback = pageCallback[0]

        firstListJosn = re.findall(
            r'(?<=<script>window.initialState=)(.*?)(?=</script>)', str(response.text))
        firstList = json.loads(firstListJosn[0])
        items = _.get(firstList, 'information.informationList.itemList')

        self.itemsImport(items)
            
        yield self.getNextQuery(pageCallback)
        
    def itemsImport(self, items):
        bulk = []
        for item in items:
            t = item['templateMaterial']

            doc = {}

            doc['title'] = t['widgetTitle']
            doc['url'] = self.domin + '/p/' + str(t['itemId'])

            doc['author'] = t['authorName']
            userId = t['authorRoute'].replace('detail_author?userId=', '')
            doc['author_url'] = self.domin + '/user/' + str(userId)

            doc['source'] = self.source
            
            if 'themeName' in t:
                doc['tag'] = t['themeName']
                
            if 'summary' in t:
                doc['summary'] = t['summary']

            date_time_obj = datetime.datetime.fromtimestamp(
                t['publishTime']/1000)

            doc['created_at'] = date_time_obj.astimezone(timezone("UTC")).strftime("%Y-%m-%dT%H:%M:%SZ")
            doc['created_year'] = date_time_obj.strftime("%Y")

            bulk.append(
                {"index": {"_index": "article"}})
            bulk.append(doc)

        if len(bulk) > 0:
            resp = self.es.client.bulk(body=bulk)
            
    def getNextQuery(self, pageCallback):
        flow_url = 'https://gateway.36kr.com/api/mis/nav/ifm/subNav/flow'
        
        payload = {
            "partner_id": "web",
            "timestamp": 1662859338075,
            "param": {
                "subnavType": 1,
                "subnavNick": "web_news",
                "pageSize": 1000,
                "pageEvent": 1,
                "pageCallback": pageCallback,
                "siteId": 1,
                "platformId": 2
            }
        }
        return scrapy.http.JsonRequest(flow_url, data=payload, callback=lambda response, payload=payload : self.nextPageParse(response, payload))
            
    def nextPageParse(self, reponse, payload):
        resp = json.loads(reponse.text)
        
        pageCallback = _.get(resp,'data.pageCallback')
        items = _.get(resp,'data.itemList')
        hasNextPage = _.get(resp,'data.hasNextPage')
        
        self.itemsImport(items)
            
        
        if hasNextPage == 1:
            yield self.getNextQuery(pageCallback)
        # pp.pprint(resp)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
