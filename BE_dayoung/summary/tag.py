from scipy.sparse import csr_matrix
from collections import defaultdict
from collections import Counter
from pykospacing import spacing
import re
import os
import sys
from konlpy.tag import Kkma
from konlpy.tag import Okt

from db_to_csv import make_csv, open_csv

from krwordrank.sentence import summarize_with_sentences


kkma = Kkma()
okt = Okt()

# db to csv(pandas)
item = input(">>> ")
try:
    make_csv(item)
    data = open_csv(item)
    print(data)
except:
    print("정보가 없음")

# 전처리

# 텍스트 cleaning


def preprocessing(text):
    text = re.sub('\n', '', text)
    text = re.sub('\xa0', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('([a-zA-Z])', '', text)
    text = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', text)
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text)
    return text

# 핵심문장 추출


def penalty(x): return 0 if (25 <= len(x) <= 80) else 1
# stopwords = {'영화', '관람객', '너무', '정말', '진짜'}


# 키워드랑 핵심문장 추출되는데, 정제 안하고 넣어볼까... stopwords 뭘로 해야할까... -> PyKoSpacing?
keywords, sents = summarize_with_sentences(
    texts,
    penalty=penalty,
    stopwords=stopwords,
    diversity=0.5,
    num_keywords=100,
    num_keysents=10,
    verbose=False
)


# 키워드 추출


# def scan_vocabulary(sents, tokenize, min_count=2):
#     counter = Counter(w for sent in sents for w in tokenize(sent))
#     counter = {w: c for w, c in counter.items() if c >= min_count}
#     idx_to_vocab = [w for w, _ in sorted(counter.items(), key=lambda x:-x[1])]
#     vocab_to_idx = {vocab: idx for idx, vocab in enumerate(idx_to_vocab)}
#     return idx_to_vocab, vocab_to_idx


# def cooccurrence(tokens, vocab_to_idx, window=2, min_cooccurrence=2):
#     counter = defaultdict(int)
#     for s, tokens_i in enumerate(tokens):
#         vocabs = [vocab_to_idx[w] for w in tokens_i if w in vocab_to_idx]
#         n = len(vocabs)
#         for i, v in enumerate(vocabs):
#             if window <= 0:
#                 b, e = 0, n
#             else:
#                 b = max(0, i - window)
#                 e = min(i + window, n)
#             for j in range(b, e):
#                 if i == j:
#                     continue
#                 counter[(v, vocabs[j])] += 1
#                 counter[(vocabs[j], v)] += 1
#     counter = {k: v for k, v in counter.items() if v >= min_cooccurrence}
#     n_vocabs = len(vocab_to_idx)
#     return dict_to_mat(counter, n_vocabs, n_vocabs)


# def dict_to_mat(d, n_rows, n_cols):
#     rows, cols, data = [], [], []
#     for (i, j), v in d.items():
#         rows.append(i)
#         cols.append(j)
#         data.append(v)
#     return csr_matrix((data, (rows, cols)), shape=(n_rows, n_cols))


# def textrank_keyword(sents, tokenize, min_count, window, min_cooccurrence, df=0.85, max_iter=30, topk=30):
#     g, idx_to_vocab = word_graph(
#         sents, tokenize, min_count, window, min_cooccurrence)
#     R = pagerank(g, df, max_iter).reshape(-1)
#     idxs = R.argsort()[-topk:]
#     keywords = [(idx_to_vocab[idx], R[idx]) for idx in reversed(idxs)]
#     return keywords

# pandas 데이터를 다시 db로...
