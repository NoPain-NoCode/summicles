-- LOAD DATA INFILE statement LOAD DATA [LOCAL] INFILE 'file_name' INTO TABLE tbl_name [CHARACTER SET charset_name] [{FIELDS | COLUMNS} [TERMINATED BY 'string'] [[OPTIONALLY] ENCLOSED BY 'char'] [ESCAPED BY 'char'] ] [LINES [STARTING BY 'string'] [TERMINATED BY 'string']
CREATE database news


LOAD DATA LOCAL INFILE "./news_crawl/news.csv"
INTO TABLE news.article FIELDS TERMINATED BY ",";


CREATE TABLE article(
    link VARCHAR(300),
    category VARCHAR(64),
    title TEXT,
    article_date DATETIME,
    img VARCHAR(256),
    contents TEXT,
    crawl_time DATETIME,
);

-- CREATE TABLE article_ec
--     AS SELECT * FROM article WHERE category