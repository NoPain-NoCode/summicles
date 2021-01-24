# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class NewscrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    source = scrapy.Field()  # 신문사
    category = scrapy.Field()  # 카테고리
    title = scrapy.Field()  # 제목
    url = scrapy.Field()  # 기사링크
    date = scrapy.Field()  # 날짜
    article = scrapy.Field()
    pass
