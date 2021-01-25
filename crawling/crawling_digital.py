# selenium 임포트
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# 이미지 바이트 처리
from io import BytesIO
import urllib.request as req
# mysql 연동
import pymysql
import datetime

# 데이터베이스에 연결
conn = pymysql.connect(host='localhost', user='root', password='root', db='mysql')
# 커서 연결
cur = conn.cursor()

def withImg (link, category, title, article_date, img, contents, crawl_time, newspaper) :
    cur.execute('insert into article(link, category, title, article_date, img, contents, crawl_time, newspaper) values (%s, %s, %s, %s, %s, %s, %s, %s)', (link, 'IT/과학', title, article_date, img, contents, crawl_time, newspaper))

def withoutImg (link, category, title, article_date, contents, crawl_time, newspaper) :
    cur.execute('insert into article(link, category, title, article_date, contents, crawl_time, newspaper) values (%s, %s, %s, %s, %s, %s, %s)', (link, 'IT/과학', title, article_date, contents, crawl_time, newspaper))

try:
    # article table에 연결
    cur.execute("use summicles")

    now = datetime.datetime.now()
    crawl_time = now.strftime('%Y. %m. %d. %H:%M')

    # 새로운 크롤링 결과를 저장하기 전에 기존의 정보 삭제
    cur.execute("delete from article where category='IT/과학'")
    conn.commit()

    chrome_options = Options()
    chrome_options.add_argument("--headless") # 실행 했을 때 브라우저가 실행되지 않는다.

    # webdriver 설정(Chrome, Firefox 등) - Headless 모드
    browser = webdriver.Chrome('D:/webdriver/chrome/chromedriver.exe', options=chrome_options)

    # webdriver 설정(Chrome, Firefox 등) - 일반 모드
    # browser = webdriver.Chrome('D:/webdriver/chrome/chromedriver.exe')

    # 크롬 브라우저 내부 대기
    browser.implicitly_wait(5)

    # 브라우저 사이즈
    browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

    # 페이지 이동
    browser.get('https://news.daum.net/digital#1')

    # 1차 페이지 내용
    # print('Before Page Contents : {}'.format(browser.page_source))

    # 현재 페이지의 기사 순서
    nth_new = 1

    # 한 페이지에서 크롤링할 기사 수
    target_crawl_news_num =20

    while nth_new <= target_crawl_news_num:
        # 페이지 이동 클릭
        WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.list_timenews > li:nth-child({}) > strong > a'.format(nth_new)))).click()

        # bs4 초기화
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        # 소스코드 정리
        # print(soup.prettify)

        # 페이지 번호 출력
        print('****** {}th New ******'.format(nth_new))

        # 필요 정보 추출(news_comp, title, date, img, contents, link)
        # 도중에 문제가 있다면 크롤링 하지 않고 넘어감.
        try:
            newspaper = soup.select('div.head_view > em > a >img')[0]['alt']
            title = soup.select('div.head_view > h3')[0].text.strip()
            article_date = soup.select('div.head_view > span.info_view > span:nth-child(2) > span.num_date')[0].text.strip()
            contents_lists = soup.select('div#harmonyContainer > section > p[dmcf-ptype="general"]')
            link = soup.select('div.copyUrl > div.sns_copyurl > a.link_copyurl > span:nth-child(2)')[0].text.strip()
            # 이미지가 없는 기사일 경우 오류처리
            try:
                img = soup.select('figure.figure_frm.origin_fig > p.link_figure > img')[0]['data-org-src']
            except IndexError as e:
                img = 0
        except IndexError as e:
            nth_new += 1
            continue

        print(newspaper)
        print(title)
        print(article_date)
        if img:
            print(soup.select('figure.figure_frm.origin_fig > p.link_figure > img')[0]['data-org-src'])
        print(link)

        # 여러 문장으로 나눠서 온 content들을 하나의 문장으로 합친다.
        contents = ''
        for content in contents_lists:
            contents += content.text.strip()
        print(contents)

        # img 정보가 있다면 넣어주고, 없다면 null로 입력
        if img:
            withImg(link, 'IT/과학', title, article_date, img, contents, crawl_time, newspaper)
        else:
            withoutImg(link, 'IT/과학', title, article_date, contents, crawl_time, newspaper)

        # 페이지 뒤로 가기
        browser.back()
        time.sleep(3)

        nth_new += 1

        print()
        print()

        # 페이지 별 스크린 샷 저장
        # browser.save_screenshot('./target_page{}.png'.format(cur_page))

        # BeautifulSoup 인스턴스 삭제
        del soup

    # 브라우저 종료
    browser.close()

    # DB에 변경사항 저장
    conn.commit()

# db 커서, 연결 해제
finally:
    cur.close()
    conn.close()