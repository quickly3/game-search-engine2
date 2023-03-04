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

sys.path.append('..')
from es.es_client import EsClient

input_file = 'os_tools_detail.csv'


csv_reader = csv.DictReader(
    open(input_file, 'r', encoding='utf-8'), delimiter=',')

es = EsClient()
count = 0
bulk = []

for data in csv_reader:
    doc = dict(data)
    doc['source'] = 'oschina'

    doc['title'] = doc['title']

    if doc['subTitle'] != '':
        doc['title'] = doc['title'] + ' - ' + doc['subTitle']

    del doc['subTitle']

    doc['tag'] = doc['tag'].split(',')

    if doc['protocol'] != '' and doc['protocol'] != '未知':
        doc['tag'].append(doc['protocol'])
    del doc['protocol']
    
    if doc['system'] != '' and doc['system'] != '未知':
        doc['tag'].append(doc['system'])
    del doc['system']
    

    doc['category'] = doc['category'].split(',')
    doc['category'].append('Software')

    if doc['location'] != '' and doc['location'] != '不详':
        doc['category'].append(doc['location'])
    del doc['location']

    if doc['isOS'] != '':
        doc['category'].append(doc['isOS'])
    del doc['isOS']


    doc['summary'] = doc['sumary']
    del doc['sumary']

    bulk.append(
        {"index": {"_index": "article"}})
    bulk.append(doc)
    count+=1

    if count == 50:
        resp = es.client.bulk(body=bulk)
        count = 0
        bulk = []   
        print(str(csv_reader.line_num) + '/61509')
    
    if csv_reader.line_num == 61509:
        es.client.bulk(body=bulk)