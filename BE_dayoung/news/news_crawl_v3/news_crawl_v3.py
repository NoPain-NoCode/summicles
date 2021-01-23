import os
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime, timedelta
from traceback import format_exc

dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(dir, './save'))

import pandas_csv
# import to_es

base_url = "http://news.naver.com/#"

class NewsCrawling:
    
    data = urlopen(base_url).read()
    soup = BeautifulSoup(data, "html.parser")
    total_data = soup.find_all(attrs={'class': 'main_component droppable'})

    colect_time = str(datetime.utcnow().replace(microsecond=0) + timedelta(hours=9))[:16]

    for each_data in total_data:

        category = ""

        try:
            category = str(each_data.find_all(attrs={'class': 'tit_sec'})).split('>')[2][:-3]
        except:
            pass

        data = str(each_data.find_all(attrs={'class': 'mlist2 no_bg'}))

        news_list = data.split('<li>')

        for each_news in news_list[1:]:

            news_block = each_news.split('href="')[1]
            # print(news_block)

            title = news_block.split('<strong>')[1].split('</strong>')[0]
            # print(title)
            news_url = news_block.split('"')[0].replace("amp;", "")
            # print(news_url)
            soup2 = BeautifulSoup(urlopen(news_url).read(), "html.parser")
            # print(soup2)

            # article_info = soup2.find_all(attrs={'class': 'article_info'})
            # print(article_info)

            article_body = str(soup2.find_all(attrs={'id': 'articleBodyContents'}))
            insert_data = {"source": "naver_news",
                           "category": category,
                           "title": title,
                           "article_body": article_body,
                           "colect_time": colect_time}

            pandas_csv.to_csv(insert_data)
            # to_es.to_elastic(insert_data)


collecting(base_url)