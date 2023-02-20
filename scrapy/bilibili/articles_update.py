import sys
sys.path.append('..')
from es.es_client import EsClient
import pydash as _
import pprint
import urllib.request as request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
pp = pprint.PrettyPrinter(indent=4)

import csv
import os


def get_tags(aid):
    url = 'https://api.bilibili.com/x/web-interface/view/detail/tag?aid={aid}'
    url = url.replace('{aid}', str(aid))
    header = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    pp.pprint(url)

    rq = request.Request(url=url, headers=header, method='GET')
    resp = request.urlopen(rq)
    data = json.loads(resp.read())
    return data

if __name__ == "__main__":
    es = EsClient()
    scrollResp = es.getDocsByQuery('source:bilibili && -tag:*')

    hits = _.get(scrollResp, 'hits.hits')

    if len(hits) > 0:
        for hit in hits:
            _id = _.get(hit,'_id')
            _source = _.get(hit,'_source')

            tagResp = get_tags(_source['sub_id'])
            tagsData = _.get(tagResp,"data")
            if tagsData:
                tags = list(map(lambda x:x['tag_name'],tagsData))
                if len(tags) > 0:
                    updResp = es.updateById(_id,{"doc":{"tag":tags}})
                    pp.pprint(updResp)
            break;
            


    # if len(toCSV) == 0:
    #     print("Found nothing!")
    #     os._exit(0)

    # scroll_id = scrollResp['scroll_id']
    # keys = toCSV[0].keys()

    # while len(scrollResp['hits']) > 0:
    #     scrollResp = es.getDocsNext(scroll_id)
    #     toCSV = toCSV + scrollResp['hits']
    #     print(len(toCSV),'/',total)

