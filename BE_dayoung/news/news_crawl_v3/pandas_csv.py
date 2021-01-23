import os
import pandas as pd
from datetime import datetime, timedelta
import configparser
import glob

config = configparser.ConfigParser()
config.read('/home/yutw/project/searchnews/crawler/crawler.conf')

def to_csv(data):

    pathlink ="/home/yutw/data/searchnews"

    # db create
    if not os.path.isdir(pathlink):
        os.mkdir(pathlink)

    present_date = str(datetime.utcnow() + timedelta(hours=9))[:10]

    # col = ["source", "category", "title", "article_body", "colect_time"]

    if len(glob.glob(pathlink + "/" + present_date + ".csv")) == 1:
        cnt = len(pd.read_csv(pathlink + "/" + present_date + ".csv", index_col=0).index)
        time_pd = pd.DataFrame(data, index=[cnt])
        time_pd.to_csv(pathlink + "/" + present_date + ".csv", mode='a', header=False)
    else:
        cnt = 0
        time_pd = pd.DataFrame(data, index=[cnt])
        time_pd.to_csv(pathlink + "/" + present_date + ".csv", mode='a')