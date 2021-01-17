import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import re

import time

url = 'http://news.daum.net/ranking/popular/'


def get_ranking_news(type='popular'):
    base_url = "http://news.daum.net/ranking/"
    url = parse.urljoin(base_url, type)
    res = requests.get(url)

    if res.status_code == 200:
        soup = BeautifulSoup(res.text)
        news_list = soup.select('ul.list_news2 div.cont_thumb')
        content_list = []

        for news in news_list:
            link = news.select_one('strong > a').get('href')
            title = news.select_one('strong > a').text.strip()
            newspaper = news.select_one('strong > span').text.strip()
            content_list.append([link, title, newspaper])

        filename = '{}_{}_new_list.csv'.format(
            type, datetime.now().strftime('%Y-%m-%d'))
        df = pd.DataFrame(content_list, columns=['link', 'title', 'newspaper'])
        df.to_csv(filename, index=False, encoding='UTF-8')
    else:
        raise Exception('sorry')


get_ranking_news('news')
