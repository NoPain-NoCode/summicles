import os
import django

# from scipy.sparse import csr_matrix
# from collections import defaultdict
# from collections import Counter
# from pykospacing import spacing
import re
import os
import sys
from konlpy.tag import Kkma
from konlpy.tag import Okt
from krwordrank.sentence import summarize_with_sentences

kkma = Kkma()
okt = Okt()

# DB에서 데이터 불러오기
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'summicles.settings')
django.setup()
from article.models import Article

data = Article.objects.all().values('contents')

# print(data[6])

# 전처리
# def preprocessing(texts):
#     text_li = []
#     for text in texts:
#         # 텍스트 cleaning
#         text = str(text)
#         text = re.sub('\[.*?\]', '', text)
#         text = re.sub('\n', '', text)
#         text = re.sub('\xa0', '', text)
#         text = re.sub('https?://\S+|www\.\S+', '', text)
#         text = re.sub('([a-zA-Z])', '', text)
#         text = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', text)
#         text = re.sub(
#             '[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》∼【】▶☞·{}]', '', text)
        
#         # Stemming
#         text = okt.pos(text, stem=True)
#         word = []
#         for i in text:
#             if not i[1] == 'Noun':
#                 continue
#             if len(i[0]) == 1:
#                 continue
#             word.append(i[0])
#         word = ' '.join(word)
#         text_li.append(word)
#         text_li.append(te)
#     return text_li

def preprocessing(text):

    # 텍스트 cleaning
    text = str(text)
    text = re.sub('\[*?\]', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\xa0', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('([a-zA-Z])', '', text)
    text = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', text)
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》∼【】▶☞·{}]', '', text)
        
    # Stemming
    text = okt.pos(text, stem=True)
    word = []
    for i in text:
        if not i[1] == 'Noun':
            continue
        if len(i[0]) == 1:
            continue
        word.append(i[0])
    word = ' '.join(word)
    return word

def make_tag(data):
    stopwords = {'기자'}

    #전처리
    text = preprocessing(data)
    #문장별로 나눠줌
    texts = text.split('.')
    tag = ''
    # 학습
    try:
        keywords, sents = summarize_with_sentences(
            texts,
            stopwords=stopwords,
            num_keywords=5,
            num_keysents=3
        )
        for word, r in sorted(keywords.items(), key=lambda x:x[1], reverse=True)[:5]:
            # print('%8s:\t%.4f' % (word, r))
            # print('#%s' % word)
            tag += '#'+word+' '
    except ValueError as v:
        # print('#')
        tag = '# '
    # tag에 추가

    return tag

def make_summary(data):
    stopwords = {'기자'}

    #전처리
    text = str(data)
    #문장별로 나눠줌
    texts = text.split('.')
    summary = ''
    # 학습
    try:
        keywords, sents = summarize_with_sentences(
            texts,
            stopwords=stopwords,
            num_keywords=5,
            num_keysents=3
        )
        for word in sorted(sents, key=lambda x:x[1], reverse=True)[:5]:
            # print('%8s:\t%.4f' % (word, r))
            # print('#%s' % word)
            summary += word+'\n'
    except ValueError as v:
        # print('#')
        summary = ''
    # tag에 추가

    return summary

# print(tag[2])


# # DB 연결아직 안됨
# def delete_all_Final():
#     queryset = ArticleFinal.objects.all()
#     queryset.delete()

# def add_new_itmes_Final(trained_items):
#     # 새로운 기사를 저장하기 전에 기존의 데이터를 모두 삭제
#     delete_all_Final()

#     last_inserted_items = ArticleFinal.objects.last()
#     if last_inserted_items is None:
#         last_inserted_link = ""
#     else:
#         last_inserted_link = getattr(last_inserted_items, 'link')
#     items_to_insert_into_db = []
#     for item in trained_items:
#         if item['link'] == last_inserted_link:
#             break
#         items_to_insert_into_db.append(item)
#     items_to_insert_into_db.reverse()
#     i = 0
#     for item in items_to_insert_into_db:
#         ArticleFinal(
#             link=item['link'],
#             category=item['category'],
#             title=item['title'],
#             article_date=item['article_date'],
#             img=item['img'],
#             contents=item['contents'],
#             crawl_time=item['crawl_time'],
#             newspaper=item['newspaper'],
#             tag = tag[i],
#         ).save()
#         i += 1
#         # print("new item added!")

#     return items_to_insert_into_db

# trained_items = Article.objects.all()
# add_new_itmes_Final(trained_items)
