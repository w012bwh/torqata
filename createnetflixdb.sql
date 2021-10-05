CREATE DATABASE netflix_data;
SET client_encoding = 'UTF8';
DROP TABLE IF EXISTS netflix_titles;

CREATE TABLE netflix_titles
(
    show_id        varchar(255),
    type           varchar(255),
    title          varchar(255),
    director       varchar(255),
    "cast"         varchar(1000),
    country        varchar(255),
    date_added     varchar(255),
    release_year   varchar(255),
    rating         varchar(255),
    duration       varchar(255),
    listed_in      varchar(255),
    description    varchar(1000),

    PRIMARY KEY (show_id)
);


\COPY netflix_titles(show_id, type, title, director, "cast", country, date_added, release_year, rating, duration, listed_in, description) FROM 'C:\torqata\netflix_titles.csv' DELIMITERS ',' CSV

UPDATE netflix_titles
SET director = 'NULL'
WHERE director IS NULL;

UPDATE netflix_titles
SET "cast" = 'NULL'
WHERE "cast" IS NULL;

UPDATE netflix_titles
SET country = 'NULL'
WHERE country IS NULL;

UPDATE netflix_titles
SET date_added = 'NULL'
WHERE date_added IS NULL;

UPDATE netflix_titles
SET release_year = 'NULL'
WHERE release_year IS NULL;

UPDATE netflix_titles
SET rating = 'NULL'
WHERE rating IS NULL;

UPDATE netflix_titles
SET duration = 'NULL'
WHERE duration IS NULL;

UPDATE netflix_titles
SET listed_in = 'NULL'
WHERE listed_in IS NULL;

UPDATE netflix_titles
SET description = 'NULL'
WHERE description IS NULL;
