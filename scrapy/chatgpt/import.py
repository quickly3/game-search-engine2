import csv
import pprint
import urllib.request as request
import json
import pydash as _
import numpy as np
import pandas as pd
import ssl
import time
from datetime import datetime
import sys
import re
sys.path.append('..')
from es.es_client import EsClient

pp = pprint.PrettyPrinter(indent=4)


csv_reader = csv.DictReader(
    open('total.csv', 'r', encoding='utf-8'), delimiter=',')

output = []

es = EsClient()
dump_to= 525585


def itemsImport(items):
    bulk = []
    for item in items:
        doc = {}
        doc['title'] = item['question']

        doc['source'] = "chatgpt"
        doc['category'] = [item['cate']]
        doc['tag'] = ['中文', '咒语']

        # break
        bulk.append(
            {"index": {"_index": "article"}})
        bulk.append(doc)
    if len(bulk) > 0:
        resp = es.client.bulk(body=bulk)


def compress_string(s):
    # 使用正则表达式将连续的重复字符替换为单个字符
    return re.sub(r"(-)\1+", r"\1", s)


items = []
counter = 0
_curr = 0

for data in csv_reader:
    _curr+=1
    if _curr <= dump_to:
        continue
    if data['cate'] == '-':
        continue

    counter += 1
    items.append(data)

    if counter == 100:
        print('Current: {}'.format(_curr))
        itemsImport(items)
        items = []
        counter=0
