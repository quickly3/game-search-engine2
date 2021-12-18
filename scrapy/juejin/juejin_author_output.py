# 导出全部juejin文章作者
from es_client import EsClient
import csv
import os

if __name__ == "__main__":

    file = 'authors.csv'

    if os.path.exists(file):
        os.remove(file)

    es = EsClient()
    toCSV = es.getAuthors()
    toCSV = sorted(toCSV, key=lambda k: k['doc_count'], reverse=True)

    keys = toCSV[0].keys()

    with open(file, 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
