from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
import json
import configparser
from datetime import datetime, timedelta
import pandas as pd

config = configparser.ConfigParser()
config.read('/home/yutw/project/searchnews/crawler/crawler.conf')

def to_elastic(data):

    pathlink = "/home/yutw/data/searchnews"

    present_date = str(datetime.utcnow() + timedelta(hours=9))[:10]
    del_date = str(datetime.utcnow() - timedelta(hours=39))[:10]

    cnt = len(pd.read_csv(pathlink + "/" + present_date + ".csv", index_col=0).index)
    es.index(index="searchnews", doc_type='naver_news', id=present_date + "-" + str(cnt), body=json.dumps(data))

    if cnt == 1:
        days = [x for x in range(1, int(del_date[-2:]))]
        for day in days:
            if len(str(day)) == 1:
                for each in range(1, 1500):
                    try:
                        es.delete(index="searchnews", doc_type="naver_news", id=del_date[:8] + '0' + str(day) + "-" + str(each))
                    except:
                        pass
            else:
                for each in range(1, 1500):
                    try:
                        es.delete(index="searchnews", doc_type="naver_news", id=del_date[:8] + str(day) + "-" + str(each))
                    except:
                        pass