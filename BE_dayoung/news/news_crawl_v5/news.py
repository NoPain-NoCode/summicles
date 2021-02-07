from korea_news_crawler.articlecrawler import ArticleCrawler

Crawler = ArticleCrawler()

Crawler.set_category("politics", "economy")
Crawler.set_date_range(2020, 1, 2020, 2)
Crawler.start()
