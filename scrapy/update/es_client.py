from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger
from dotenv import load_dotenv
import os

es_logger.setLevel(50)

class EsClient:

    def __init__(self):
        load_dotenv("../../.env")
        es_user = os.getenv("ES_USER")
        es_pwd = os.getenv("ES_PWD")
        self.client = Elasticsearch(http_auth=(es_user, es_pwd))

    def getDocs(self):
        query = {
            "query": {
                "query_string": {
                    "query": "source:juejin && -author_url:*"
                }
            },
            "size": 1000,
            "_source": ["url","source"]
        }

        resp = self.client.search(index="article", body=query, scroll='2m')
        result = self.formatResp(resp);
        return result
        
    def getDocsNext(self, scroll_id):
        resp = self.client.scroll(scroll_id=scroll_id, scroll='2m')
        result = self.formatResp(resp);
        return result

    def formatResp(self,resp):
        result = {}

        if len(resp['hits']['hits']) == 0:
            result['scroll_id'] = ""
            result['hits'] = []
        else:
            result['scroll_id'] = resp['_scroll_id']
            result['hits'] = list(map(lambda x: dict(id=x['_id'],source=x['_source']['source'],url=x['_source']['url']),resp['hits']['hits']))

        return result;