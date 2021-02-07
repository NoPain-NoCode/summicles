DROP DATABASE IF EXISTS articles;
CREATE DATABASE IF NOT EXISTS articles;
USE articles;

DROP TABLE IF EXISTS articles;
CREATE TABLE articles(
    link            VARCHAR(255) NOT NULL,
    category        VARCHAR(64),
    title           VARCHAR(255),
    article_date    VARCHAR(128),
    img             VARCHAR(255),
    contents        TEXT,
    crawl_time      VARCHAR(128),
    newspaper       VARCHAR(64),
    PRIMARY KEY (link)
);

