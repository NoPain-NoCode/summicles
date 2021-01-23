-- LOAD DATA INFILE statement LOAD DATA [LOCAL] INFILE 'file_name' INTO TABLE tbl_name [CHARACTER SET charset_name] [{FIELDS | COLUMNS} [TERMINATED BY 'string'] [[OPTIONALLY] ENCLOSED BY 'char'] [ESCAPED BY 'char'] ] [LINES [STARTING BY 'string'] [TERMINATED BY 'string']


CREATE TABLE article(
    link VARCHAR(300) NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    summary TEXT,
    tag  VARCHAR(128),
    img ,
    category VARCHAR(64),
    newspaper VARCHAR(128), 
)

CREATE TABLE article_ec
    AS SELECT * FROM article WHERE category