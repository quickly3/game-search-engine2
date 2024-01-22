from elasticsearch import Elasticsearch
from elasticsearch import logger as es_logger
from dotenv import load_dotenv
import os
import logging

logging.getLogger("urllib3").setLevel(logging.ERROR)

es_logger.setLevel(50)


class EsClient:

    def __init__(self):
        load_dotenv("../../.env")
        es_user = os.getenv("ES_USER")
        es_pwd = os.getenv("ES_PWD")
        ES_HOST = os.getenv("ES_HOST")
        ES_PORT = os.getenv("ES_PORT")
        host = ES_HOST+":"+ES_PORT;


        self.client = Elasticsearch(host, http_auth=(es_user, es_pwd))

    def getDocs(self):
        query = {
            "query": {
                "query_string": {
                    "query": "source:juejin && -author_id:*"
                }
            },
            "size": 1000,
            "_source": ["url", "source"]
        }

        resp = self.client.search(index="article", body=query, scroll='2m')
        result = self.formatResp(resp)
        return result

    def index(self,doc):
        self.client.index(index="article", document=doc)
    
    def getTeamIds(self):
        query = {
            "query": {
                "query_string": {
                    "query": "tech_team:*"
                }
            },
            "_source": [
                "tech_team.org_id"
            ],
            "size": 300
        }

        resp = self.client.search(index="author", body=query)
        ids = list(map(lambda x:x['_source']['tech_team']['org_id'], resp['hits']['hits']))
        return ids

    def articleExisted(self,url):
        query = {
            "query": {
                "query_string": {
                    "query": "url:\""+url+"\""
                }
            }
        }

        resp = self.client.count(index="article", body=query)
        return resp['count'] > 0


    def getAuthors(self,field = 'author_url'):
        fisrt_query = {
            "query": {
                "query_string": {
                    "query": "source:juejin"
                }
            },
            "size": 0,
            "aggs": {
                "author_buckets": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {
                                "author_url": {
                                    "terms": {
                                        "field": field
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        }
        resp = self.client.search(index="article", body=fisrt_query)
        result = self.formatCompositeTermsAgg(resp)
        list = []
        
        if result:
            list = result['hits']
            print(len(list))

            if 'after_key' in result:
                after_key = result['after_key']
                while result :
                    result = self.getAuthorsByAfterKey(after_key, field)
                    if result:
                        list = list + result['hits']
                        print(len(list))
                        if 'after_key' in result:
                            after_key = result['after_key']
                        else:
                            break;

        return list

    def getAuthorsByAfterKey(self, after_key, field):
        after_query = {
            "track_total_hits":True,
            "query": {
                "query_string": {
                    "query": "source:juejin"
                }
            },
            "size": 0,
            "aggs": {
                "author_buckets": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {
                                "author_url": {
                                    "terms": {
                                        "field": field
                                    }
                                }
                            }
                        ],
                        "after":after_key
                    }
                }
            }
        }
        resp = self.client.search(index="article", body=after_query)
        result = self.formatCompositeTermsAgg(resp)
        return result

    def getAuthorsFromFollowees(self):
        fisrt_query = {
            "query": {
                "query_string": {
                    "query": "source:juejin"
                }
            },
            "size": 0,
            "aggs": {
                "author_buckets": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {
                                "followee_id": {
                                    "terms": {
                                        "field": 'followee_id'
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        }
        resp = self.client.search(index="followees", body=fisrt_query)
        result = self.formatCompositeTermsAgg2(resp)
        list = []
        
        if result:
            list = result['hits']
            print(len(list))
            if 'after_key' in result:
                after_key = result['after_key']
                while result :
                    result = self.getAuthorsByAfterKeyFromFollowees(after_key)
                    if result:
                        list = list + result['hits']
                        print(len(list))
                        if 'after_key' in result:
                            after_key = result['after_key']
                        else:
                            break;

        return list


    def getAuthorsFromFollowers(self):
        fisrt_query = {
            "query": {
                "query_string": {
                    "query": "source:juejin"
                }
            },
            "size": 0,
            "aggs": {
                "author_buckets": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {
                                "followee_id": {
                                    "terms": {
                                        "field": 'followee_id'
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        }

        print('body', fisrt_query)
        resp = self.client.search(index="followers", body=fisrt_query)
        result = self.formatCompositeTermsAgg2(resp)
        list = []
        
        if result:
            list = result['hits']
            print(len(list))
            if 'after_key' in result:
                after_key = result['after_key']
                while result :
                    result = self.getAuthorsByAfterKeyFromFollowers(after_key)
                    if result:
                        list = list + result['hits']
                        print(len(list))
                        if 'after_key' in result:
                            after_key = result['after_key']
                        else:
                            break;

        return list

    def getAuthorsByAfterKey(self, after_key, field):
        after_query = {
            "track_total_hits":True,
            "query": {
                "query_string": {
                    "query": "source:juejin"
                }
            },
            "size": 0,
            "aggs": {
                "author_buckets": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {
                                "author_url": {
                                    "terms": {
                                        "field": field
                                    }
                                }
                            }
                        ],
                        "after":after_key
                    }
                }
            }
        }
        resp = self.client.search(index="article", body=after_query)
        result = self.formatCompositeTermsAgg(resp)
        return result

    def getAuthorsByAfterKeyFromFollowees(self, after_key):
        after_query = {
            "track_total_hits":True,
            "query": {
                "query_string": {
                    "query": "source:juejin"
                }
            },
            "size": 0,
            "aggs": {
                "author_buckets": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {
                                "followee_id": {
                                    "terms": {
                                        "field": 'followee_id'
                                    }
                                }
                            }
                        ],
                        "after":after_key
                    }
                }
            }
        }
        resp = self.client.search(index="followees", body=after_query)
        result = self.formatCompositeTermsAgg2(resp)
        return result

    def getAuthorsByAfterKeyFromFollowers(self, after_key):
        after_query = {
            "track_total_hits":True,
            "query": {
                "query_string": {
                    "query": "source:juejin"
                }
            },
            "size": 0,
            "aggs": {
                "author_buckets": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {
                                "followee_id": {
                                    "terms": {
                                        "field": 'followee_id'
                                    }
                                }
                            }
                        ],
                        "after":after_key
                    }
                }
            }
        }
        resp = self.client.search(index="followers", body=after_query)
        result = self.formatCompositeTermsAgg2(resp)
        return result

    def getDocsNext(self, scroll_id):
        resp = self.client.scroll(scroll_id=scroll_id, scroll='2m')
        result = self.formatResp(resp)
        return result

    def updateById(self, id, body):
        return self.client.update(index="article", id=id, body=body)

    def deleteById(self, id):
        return self.client.delete(index="article", id=id)

    def formatCompositeTermsAgg(self, resp):
        result = {}
        buckets = resp['aggregations']['author_buckets'];

        if len(buckets) > 0:
            if 'after_key' in buckets:
                result['after_key'] =  buckets['after_key']

            result['hits'] = list(map(lambda x:dict(author_url=x['key']['author_url'], doc_count=x['doc_count']) ,buckets['buckets']))
            return result;
        else:
            return False
        
    def formatCompositeTermsAgg2(self, resp):
        result = {}
        buckets = resp['aggregations']['author_buckets'];

        if len(buckets) > 0:
            if 'after_key' in buckets:
                result['after_key'] =  buckets['after_key']

            result['hits'] = list(map(lambda x:dict(followee_id=x['key']['followee_id'], doc_count=x['doc_count']) ,buckets['buckets']))
            return result;
        else:
            return False

    def formatResp(self, resp):
        result = {}

        if len(resp['hits']['hits']) == 0:
            result['scroll_id'] = ""
            result['hits'] = []
        else:
            result['scroll_id'] = resp['_scroll_id']
            result['total'] = resp['hits']['total']
            result['hits'] = list(map(lambda x: dict(
                id=x['_id'], source=x['_source']['source'], url=x['_source']['url']), resp['hits']['hits']))

        return result
