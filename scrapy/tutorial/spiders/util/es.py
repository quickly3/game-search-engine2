# -*- coding:UTF-8 -*-
#
#

from elasticsearch import Elasticsearch
import os

# settings.py

class ElasticService():
    def __init__(self):
        es_user = os.getenv("ES_USER")
        es_pwd = os.getenv("ES_PWD")
        self.client = Elasticsearch(http_auth=(es_user, es_pwd))


def get_es():
    pass
