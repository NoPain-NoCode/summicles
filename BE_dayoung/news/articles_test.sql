DROP DATABASE IF EXISTS news_test;
CREATE DATABASE IF NOT EXISTS news_test;
USE news_test;

DROP TABLE IF EXISTS article_test;
CREATE TABLE article_test(
    link        VARCHAR(300)    NOT NULL,
    title       TEXT            NOT NULL,
    newspaper   VARCHAR(64)     NOT NULL,
    PRIMARY KEY (link)
);

LOAD DATA LOCAL INFILE './news_crawl_v2/popular_2021-01-17_new_list.csv'
INTO TABLE news_test.article_test FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';