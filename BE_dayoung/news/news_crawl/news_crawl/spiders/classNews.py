import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import ArticleItems


class NewsSpider(CrawlSpider):
    name = 'classNews'
    # 허용 도메인
    allowed_domains = ['news.daum.net']
    # 시작 URL
    start_urls = ['https://news.daum.net/ranking/popular/news',
                  'https://news.daum.net/ranking/popular/entertain', 'https://news.daum.net/ranking/popular/sports']

    # rules = [
    #     # 뉴스 메인페이지
    #     # 테스트 시 : page=\d$ 수정
    #     Rule(LinkExtractor(allow=r'ranking/popular/news\?page=\d$'),
    #          callback='parse_parent'),
    # ]

    # INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
    # 이 오류는 내가 뭔가 html 태그를 잘못 걸어서 그런거라고 함...

    def parse_parent(self, response):
        # 부모 상세 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)

        # 페이지내 신문 상세 요청
        for url in response.css('ul.list_news2 > li > div.cont_tumb'):
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
        category = response.css('h2.screen_out::text').get().strip()
        # 기사 일자
        article_date = response.css(
            'span.info_view > span.txt_info > span.num_date').get().strip()
        # 헤드라인
        title = response.css('h3.tit_view::text').get().strip()
        # 이미지
        img = response.css(
            'div.article_view > p.link_figure > img::attr(href)').get().strip()
        # 본문
        c_list = response.css('div.article_view p::text').get()
        # 리스트 -> 문자열 변경
        contents = ''.join(c_list).strip()

        yield ArticleItems(link=response.url, category=category, title=title, article_date=article_date, img=img, contents=contents)
