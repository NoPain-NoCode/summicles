import pymysql
import csv
import pandas as pd

# mysql과 연동
conn = pymysql.connect(
    host='', user='', password='Al8730956!', db='', charset='utf8')

curs = conn.cursor()

# 데이터를 읽어와서 저장


def make_csv(feature):
    # 컬럼 명 가져오기
    column = []
    sql = "show full columns from %s" % feature
    curs.execute(sql)
    rows = curs.fetchall()
    for i in range(len(rows)):
        column.append(rows[i][0])

    # 쿼리문 직접 돌리는 작업
    sql = "select * from %s" % feature
    curs.execute(sql)
    rows = curs.fetchall()

    # 데이터 타입을 list형태로 바꾸는 작업
    # DBMS에서 가져온 데이터는 튜플형식이기 때문에 list로 바꿔주어야 함.
    rows = list(rows)
    for a in range(len(rows)):
        rows[a] = list(rows[a])

    # 데이터 작성해서 저장
    f = open('%s.csv' % feature, 'w', encoding='utf-8', newline='')

    # CSV파일 입력
    wr = csv.writer(f)

    # 컬럼 명 입력
    wr.writerow(column)

    # 나머지 데이터 입력
    for i in range(len(rows)):
        wr.writerow(rows[i])
    f.close()

    # 연결해제
    conn.close()

# 데이터 읽어오는 작업


def open_csv(feature):
    f = open('%s.csv' % feature, 'r', encoding='utf-8')
    data = pd.read_csv(f)
    return data


if __name__ == "__main__":
    item = input(">>> ")
    try:
        make_csv(item)
        data = open_csv(item)
        print(data)
    except:
        print("정보가 없음")
