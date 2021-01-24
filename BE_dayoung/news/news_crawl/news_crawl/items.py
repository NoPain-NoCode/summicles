# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItems(scrapy.Item):
    # 기사 링크
    link = scrapy.Field()
    # 카테고리
    catecory = scrapy.Field()
    # 기사 제목
    title = scrapy.Field()
    # 기사 일자
    article_date = scrapy.Field()
    # 기사 이미지 링크
    img = scrapy.Field()
    # 기사 본문
    contents = scrapy.Field()
    # 수집 된 시간
    crawled_time = scrapy.Field()
