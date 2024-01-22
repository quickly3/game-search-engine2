# 导出全部juejin文章作者
from es_client import EsClient
import csv
import os

if __name__ == "__main__":

    file = 'authors3.csv'

    if os.path.exists(file):
        os.remove(file)

    es = EsClient()
    toCSV = es.getAuthorsFromFollowers()
    toCSV = sorted(toCSV, key=lambda k: k['doc_count'], reverse=True)

    toCSV2 = list(map(lambda x: {'followee_id': x['followee_id']}, toCSV))
    keys = toCSV2[0].keys()

    with open(file, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV2)
