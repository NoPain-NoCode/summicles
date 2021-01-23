import scrapy


class NewsSpider(scrapy.Spider):
    name = 'classNews'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/']

    def parse(self, response):
        titles =
