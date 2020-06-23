# -*- coding:UTF-8 -*-
#
#

from elasticsearch import Elasticsearch
import os

# settings.py
es_user = os.getenv("ES_USER")
es_pwd = os.getenv("ES_PWD")

es = Elasticsearch(http_auth=(es_user, es_pwd))
