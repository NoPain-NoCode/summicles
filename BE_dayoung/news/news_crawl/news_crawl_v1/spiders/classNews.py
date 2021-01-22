import scrapy


class NewsSpider(scrapy.Spider):
    name = 'classNews'
    allowed_domains = ['news.daum.net']
    start_urls = ['http://news.daum.net/ranking/popular/']

    def parse(self, response):
        titles = 
        
