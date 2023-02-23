import scrapy
import pprint
from scrapy.crawler import CrawlerProcess
import pandas as pd
from urllib.parse import urlencode
import csv
import pydash as _

pp = pprint.PrettyPrinter(indent=4)


lang_file = csv.DictReader(
    open('os_tools_lang_list.csv', 'r', encoding='utf-8'), delimiter=',')
tag_file = csv.DictReader(
    open('os_tools_tag_list.csv', 'r', encoding='utf-8'), delimiter=',')

urls = []

for data in lang_file:
    urls.append(data['url'])

for data in tag_file:
    urls.append(data['url'])

urls = _.uniq(urls)
url_objs = list(map(lambda x: {'url': x} , urls))

dfSg = pd.DataFrame(url_objs)
dfSg.to_csv('os_tools_list.csv', mode='a', encoding='utf-8',
            index=False, header=False)
