import csv
import os
import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch()
index = "app_test4"
count = 0
max = 1000
filePath = 'F:\download\company_des_industry.csv'
filePath2 = 'F:\download\company_des_industry2.csv'


datas = pd.read_csv(filePath)

f1 = open(filePath2, 'w', encoding="utf-8")


bulk = []
for ind, row in datas.iterrows():
    des = str(row['description'])
    if des != "nan":
        count += 1
        doc = {}
        doc['text1'] = des
        f1.write(des)
        bulk.append({"index": {"_index": index}})
        bulk.append(doc)

    if count == max:
        break
f1.close()
# if len(bulk) > 0:
#     resp = es.bulk(index="index", body=bulk, routing=1)
