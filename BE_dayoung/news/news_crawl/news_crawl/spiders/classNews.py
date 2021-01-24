import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ArticleItems


# 페이지 + 상세 페이지 크롤링 추가
# 미들웨어 설치 : pip install scrapy_fake_useragent
class NewsSpider(CrawlSpider):
    name = 'classNews'
    # 허용 도메인
    allowed_domains = ['news.daum.net']
    # 시작 URL(2페이지로 변경)
    start_urls = ['https://news.daum.net/breakingnews/society']

    rules = [
        # 뉴스 메인페이지
        # 테스트 시 : page=\d$ 수정
        Rule(LinkExtractor(allow=r'/breakingnews/society\?page=\d$'),
             callback='parse_parent'),
    ]

    def parse_parent(self, response):
        # 부모 상세 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)

        # 페이지내 신문 상세 요청
        for url in response.css('ul.list_news2 list_allnews > li > div'):
            # 신문 기사 URL
            article_url = url.css('strong > a::attr(href)').get().strip()
            # 요청
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url})

    def parse_child(self, response):
        # 부모, 자식 수신 정보 로깅
        self.logger.info('-------------------------------------------')
        self.logger.info('Response From Parent URL : %s' %
                         response.meta['parent_url'])
        self.logger.info('Child Response URL : %s' % response.url)
        self.logger.info('Child Response Status : %s' % response.status)
        self.logger.info('-------------------------------------------')

        # 카테고리
        category = response.css('').get().strip()
        # 기사 일자
        article_date = response.css('').get().strip()
        # 헤드라인
        title = response.css('h3.tit_view::text').get().strip()
        # 이미지
        img = response.css('').get().strip()
        # 본문
        c_list = response.css('div.article_view p::text').get()
        # 리스트 -> 문자열 변경
        contents = ''.join(c_list).strip()

        yield ArticleItems(link=response.url, category=category, title=title, article_date=article_date, img=img, contents=contents)
