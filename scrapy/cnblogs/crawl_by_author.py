import scrapy
from pydispatch import dispatcher
from scrapy import signals
import sys
from scrapy.crawler import CrawlerProcess
import csv
sys.path.append("../esservices");
import esClient
import copy
import re
import datetime
import pprint


pp = pprint.PrettyPrinter(indent=4)


# 根据cnblogs作者爬取全部文章
class TestSpider(scrapy.Spider):
    name = 'cnblogs_crawl_by_author'
    domin = 'https://www.cnblogs.com'
    handle_httpstatus_list = [ 500]
    current = 0
    total = 0

    source = 'cnblogs'
    mode0List = []
    simpleMode = []

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def start_requests(self):
        file = 'authors.csv'
        self.es = esClient.createClient()

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            _list = list(reader)
            self.total = len(_list)
            for item in _list:
            # for item in [_list[1]]:
                self.current = self.current+1
                _current = copy.copy(self.current)
                url = item['author_url']
                # url = 'https://www.cnblogs.com/pwindy' #3
                # url = 'https://www.cnblogs.com/GKLBB/' #1

                # url = 'https://www.cnblogs.com/xiangshihua/' #2

                # url = 'https://www.cnblogs.com/huaweiyun/' #4

                # url = 'https://www.cnblogs.com/xhlqss/'

                # url = 'https://www.cnblogs.com/morehair/'
                
                # url = 'https://www.cnblogs.com/pythonywy/'

                # url = 'https://www.cnblogs.com/dragonfei'

                # url = 'https://www.cnblogs.com/jzz-111jy/'

                yield scrapy.Request(url, callback=lambda response, url=url : self.parse(response, url))

    def parse(self, response, url): 

        match_mode = 0
        postsModes = [
            '//*[@class="post"]',
            '//*[@class="post post-list-item"]',
            '//*[@class="postlist"]',
            '//*[@class="day"]',
            '//*[@id="mainContent"]/div[2]/div[1]/div[@class="custom-card"]',
        ]

        for mode_index,mode in enumerate(postsModes):
            items = response.xpath(mode)
            if len(items) > 0:
                match_mode = mode_index + 1
                break
        
        items = response.xpath('//*[@id="mainContent"]/div/div[@class="day"]')
        if len(items) > 0:
            match_mode = 4

        bulk = []
        resp = self.getDocByMode(match_mode, response, url)

        if resp and len(resp['docs']) > 0:
            
            for doc in resp['docs']:
                bulk.append(
                    {"index": {"_index": "article"}})
                    
                doc['source'] = 'cnblogs';
                doc['valid'] = True
                
                bulk.append(doc)

            if len(bulk) > 0:
                es_resp = self.es.client.bulk(index="article", body=bulk)
                if es_resp['errors']:
                    for es_resp in es_resp['items']:
                        print('Es status',es_resp['index']['status'])


            if 'next_page_url' in resp:
                next_page_url = resp['next_page_url']
                print('next_page_url ', next_page_url)
                if next_page_url:
                    yield scrapy.Request(next_page_url, callback=lambda response, url=url : self.parse(response, url))

        else:
            print("None return")

    def getDocByMode(self, match_mode, response, author_url):

        p1 = re.compile(r'[(](.*?)[)]', re.S) 

        docs = []

        # print(match_mode, response, author_url)

        # if match_mode == 0:
        print("match_mode", match_mode, author_url)

        if match_mode == 1:
            titles = response.xpath('//a[@class="postTitle2 vertical-middle"]/span/text()').getall()
            titles = list(map(lambda x:x.strip(), titles))
            titles = list(filter(lambda x:x != '', titles))
            docs = list(map(lambda x:{'title':x}, titles))

            links = response.xpath('//a[@class="postTitle2 vertical-middle"]/@href').getall()

            sumarys = response.xpath('//div[@class="c_b_p_desc"]/text()').getall()
            sumarys = list(filter(lambda x:x != '', sumarys))
            sumarys = list(map(lambda x:x.replace('摘要：','').strip(), sumarys))


            descs = response.xpath('//p[@class="postfoot"]/text()').getall()
            descs = list(filter(lambda x:x.strip() != '', descs))
            descs = list(map(lambda x:x.replace('posted @','').strip(), descs))

            counters = response.xpath('//p[@class="postfoot"]/span/text()').getall()

            if len(descs) == 0:
                descs = response.xpath('//div[@class="itemdesc"]/text()').getall()
                descs = list(filter(lambda x:x.strip() != '', descs))
                descs = list(map(lambda x:x.replace('posted @','').strip(), descs))

                counters = response.xpath('//div[@class="itemdesc"]/span/text()').getall()

            if len(descs) == 0:
                descs = response.xpath('//div[@class="postFoot"]/text()').getall()
                descs = list(filter(lambda x:x.strip() != '', descs))
                descs = list(map(lambda x:x.replace('posted @','').strip(), descs))

                counters = response.xpath('//div[@class="postFoot"]/span/text()').getall()

            if len(descs) == 0:
                descs = response.xpath('//div[@class="author"]/text()').getall()
                descs = list(filter(lambda x:x.strip() != '', descs))
                descs = list(map(lambda x:x.replace('posted @','').strip(), descs))

                counters = response.xpath('//div[@class="author"]/span/text()').getall()

            for i,doc in enumerate(docs):
                doc['url'] = links[i]
                
                doc['summary'] = sumarys[i]

                doc['source'] = self.source
                doc['author_url'] = author_url

                descs_arr = str.split(descs[i],"\n")
                doc['author'] = descs_arr[1]
                created_at = descs_arr[0]

                date_time_obj_tz = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M')+datetime.timedelta(hours=-8)

                doc['created_at'] = date_time_obj_tz.strftime("%Y-%m-%dT%H:%M:%SZ")

                view_count_match = re.findall(p1, counters[i*3])
                comment_count_match = re.findall(p1, counters[i*3+1])
                digg_count_match = re.findall(p1, counters[i*3+2])

                doc['view_count'] =  view_count_match[0] if len(view_count_match) > 0 else 0
                doc['comment_count'] = comment_count_match[0] if len(comment_count_match) > 0 else 0
                doc['digg_count'] = digg_count_match[0] if len(digg_count_match) > 0 else 0

            next_page_url = response.xpath('//div[@id="nav_next_page"]/a/@href').get()
            if not next_page_url:
                pager_text = response.xpath('//div[@class="pager"]/a[last()]/text()').get()
                if pager_text and pager_text.strip()=='下一页':
                    next_page_url = response.xpath('//div[@class="pager"]/a[last()]/@href').get()
            
            return {
                "docs":docs,
                "next_page_url":next_page_url
            }

        if match_mode == 2:
            titles = response.xpath('//div[@class="post post-list-item"]/h2/a/span/text()').getall()
            titles = list(map(lambda x:x.strip(), titles))
            titles = list(filter(lambda x:x != '', titles))
            docs = list(map(lambda x:{'title':x}, titles))

            links = response.xpath('//div[@class="post post-list-item"]/h2/a/@href').getall()

            sumarys = response.xpath('//div[@class="c_b_p_desc"]/text()').getall()
            sumarys = list(filter(lambda x:x != '', sumarys))
            sumarys = list(map(lambda x:x.replace('摘要：','').strip(), sumarys))

            descs = response.xpath('//div[@class="post post-list-item"]/small/text()').getall()
            descs = list(filter(lambda x:'by' in x, descs))

            view_counts = response.xpath('//span[@class="post-view-count"]/text()').getall()
            digg_counts = response.xpath('//span[@class="post-digg-count"]/text()').getall()

            for i,doc in enumerate(docs):
                doc['url'] = links[i]
                
                doc['summary'] = sumarys[i]

                doc['source'] = self.source
                doc['author_url'] = author_url
                
                descs_arr = str.split(descs[i],"by")
                doc['author'] = descs_arr[1].strip()
                created_at = descs_arr[0].replace(",","").strip()

                date_time_obj_tz = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M') + datetime.timedelta(hours=-8)

                doc['created_at'] = date_time_obj_tz.strftime("%Y-%m-%dT%H:%M:%SZ")

                doc['view_count'] = view_counts[i]
                doc['digg_count'] = digg_counts[i]
                doc['comment_count'] = 0

            next_page_url = response.xpath('//div[@id="nav_next_page"]/a/@href').get()
            if not next_page_url:
                pager_text = response.xpath('//div[@class="pager"]/a[last()]/text()').get()
                if pager_text and pager_text.strip()=='下一页':
                    next_page_url = response.xpath('//div[@class="pager"]/a[last()]/@href').get()
            return {
                "docs":docs,
                "next_page_url":next_page_url
            }

        if match_mode == 3:
            titles = response.xpath('//div[@class="posttitle"]/a/span/text()').getall()
            titles = list(map(lambda x:x.strip(), titles))
            titles = list(filter(lambda x:x != '', titles))
            docs = list(map(lambda x:{'title':x}, titles))

            links = response.xpath('//div[@class="posttitle"]/a/@href').getall()
            sumarys = response.xpath('//div[@class="c_b_p_desc"]/text()').getall()
            sumarys = list(filter(lambda x:x != '', sumarys))
            sumarys =  list(map(lambda x:x.replace('摘要：','').strip(), sumarys))

            descs = response.xpath('//div[@class="itemdesc"]/text()').getall()
            descs = list(map(lambda x:x.replace('posted @','').strip(), descs))
            descs = list(filter(lambda x:x != '', descs))

            counters = response.xpath('//div[@class="itemdesc"]/span/text()').getall()

            for i,doc in enumerate(docs):
                doc['url'] = links[i]
                doc['summary'] = sumarys[i]

                doc['source'] = self.source
                doc['author_url'] = author_url

                descs_arr = str.split(descs[i],"\n")
                doc['author'] = descs_arr[1]
                created_at = descs_arr[0]

                date_time_obj_tz = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M')+datetime.timedelta(hours=-8)

                doc['created_at'] = date_time_obj_tz.strftime("%Y-%m-%dT%H:%M:%SZ")

                view_count_match = re.findall(p1, counters[i*3])
                comment_count_match = re.findall(p1, counters[i*3+1])
                digg_count_match = re.findall(p1, counters[i*3+2])

                doc['view_count'] =  view_count_match[0] if len(view_count_match) > 0 else 0
                doc['comment_count'] = comment_count_match[0] if len(comment_count_match) > 0 else 0
                doc['digg_count'] = digg_count_match[0] if len(digg_count_match) > 0 else 0

            next_page_url = response.xpath('//div[@id="nav_next_page"]/a/@href').get()
            if not next_page_url:
                pager_text = response.xpath('//div[@class="pager"]/a[last()]/text()').get()
                if pager_text and pager_text.strip()=='下一页':
                    next_page_url = response.xpath('//div[@class="pager"]/a[last()]/@href').get()
            
            return {
                "docs":docs,
                "next_page_url":next_page_url
            }

        if match_mode == 4:
            post_locked = False
            docs = []

            items = response.xpath('//*[@class="day"]')

            for item in items:
                doc = {}
                titles = item.xpath('div[@class="postTitle"]/a[@class="postTitle2 vertical-middle"]/span/text()').getall()
                titles = list(map(lambda x:x.strip(), titles))
                titles = list(filter(lambda x:x != '', titles))
                links = item.xpath('div[@class="postTitle"]/a[@class="postTitle2 vertical-middle"]/@href').getall()

                sumarys = item.xpath('div[@class="postCon"]/div[@class="c_b_p_desc"]/text()').getall()

                if not sumarys:
                    sumarys = item.xpath('div[@class="c_b_p_desc"]/text()').getall()

                if not sumarys:
                    continue

                sumarys = list(filter(lambda x:x != '', sumarys))
                sumarys =  list(map(lambda x:x.replace('摘要：','').replace('该文被密码保护。','').strip(), sumarys))
                sumarys = list(filter(lambda x:x != '', sumarys))

                descs = item.xpath('div[@class="postDesc"]/text()').getall()
                descs = list(map(lambda x:x.replace('posted @','').strip(), descs))
                descs = list(filter(lambda x:x != '', descs))

                counters = item.xpath('div[@class="postDesc"]/span/text()').getall()

                _docs = list(map(lambda x:{'title':x}, titles))


                for i,doc in enumerate(_docs):
                    doc['url'] = links[i]

                    if post_locked:
                        doc['summary'] = '无'
                    else:
                        if i in sumarys:
                            doc['summary'] = sumarys[i]

                    doc['source'] = self.source
                    doc['author_url'] = author_url

                    descs_arr = str.split(descs[i],"\n")
                    doc['author'] = descs_arr[1]
                    created_at = descs_arr[0]

                    date_time_obj_tz = datetime.datetime.strptime(created_at, '%Y-%m-%d %H:%M')+datetime.timedelta(hours=-8)

                    doc['created_at'] = date_time_obj_tz.strftime("%Y-%m-%dT%H:%M:%SZ")

                    view_count_match = re.findall(p1, counters[i*3])
                    comment_count_match = re.findall(p1, counters[i*3+1])
                    digg_count_match = re.findall(p1, counters[i*3+2])

                    doc['view_count'] =  view_count_match[0] if len(view_count_match) > 0 else 0
                    doc['comment_count'] = comment_count_match[0] if len(comment_count_match) > 0 else 0
                    doc['digg_count'] = digg_count_match[0] if len(digg_count_match) > 0 else 0

                    docs.append(doc)

            next_page_url = response.xpath('//div[@id="nav_next_page"]/a/@href').get()
            if not next_page_url:
                pager_text = response.xpath('//div[@class="pager"]/a[last()]/text()').get()
                if pager_text and pager_text.strip()=='下一页':
                    next_page_url = response.xpath('//div[@class="pager"]/a[last()]/@href').get()

            return {
                "docs":docs,
                "next_page_url":next_page_url
            }


        return None

    # def modeCheck(self)
    def spider_closed(self, spider):
        textfile = open("valid_url.txt", "w")
        for element in self.mode0List:
            textfile.write(element + "\n")
        textfile.close()

        f2 = open("simple_url.txt", "w")
        for element in self.simpleMode:
            f2.write(element + "\n")
        f2.close()



if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()
