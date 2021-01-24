CREATE database news_test;
use news_test;

CREATE TABLE article_test(link VARCHAR(300), title TEXT, newspaper VARCHAR(64));

LOAD DATA LOCAL INFILE './news_crawl_v2/kkomkkom_2021-01-17_new_list.csv' 
INTO TABLE news_test.article_test FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';