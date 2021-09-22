from es_client import EsClient
import csv
import os

if __name__ == "__main__":

    file = 'query.csv'

    if os.path.exists(file):
        os.remove(file)

    toCSV = []
    es = EsClient()
    scrollResp = es.getDocs()
    toCSV = toCSV + scrollResp['hits']

    total = scrollResp['total']['value']


    if len(toCSV) == 0:
        print("Found nothing!")
        os._exit(0)

    scroll_id = scrollResp['scroll_id']
    keys = toCSV[0].keys()

    while len(scrollResp['hits']) > 0:
        scrollResp = es.getDocsNext(scroll_id)
        toCSV = toCSV + scrollResp['hits']
        print(len(toCSV),'/',total)


    with open(file, 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
