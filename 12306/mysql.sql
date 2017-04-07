
CREATE database 12306_train;

use 12306_train;

CREATE TABLE train_info(
  train_code VARCHAR(32) NOT NULL ,
  start_staion VARCHAR(32) NOT NULL ,
  end_station VARCHAR(32) NOT NULL
);

INSERT INTO train_info VALUES ('G1002','深圳','武汉');

SELECT `train_code`, `start_staion`, `end_station` FROM train_info;


create table shop_station(
provice varchar(50) not null default '--',
city varchar(200) not null default '--',
area varchar(200) not null default '--',
name varchar(200) not null default '--',
addr varchar(200) not null default '--',
count varchar(10) not null default '--',
shoptime varchar(50) not null default '--'
);

load data infile 'D:\\MySQL\\11dsd.txt'
into table shop_station
fields terminated by ' '  optionally enclosed by '"' escaped by '"'
lines terminated by '\r\n';


# 改进
CREATE TABLE agencys (
  province VARCHAR(10) NOT NULL ,
  city VARCHAR(15) NOT NULL ,
  county VARCHAR(15) NOT NULL ,
  address VARCHAR(200) PRIMARY KEY ,
  name VARCHAR(200) NOT NULL ,
  windows INT,
  start TIME,
  end TIME
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# stations
DROP TABLE stations;
CREATE TABLE stations (
  bureau VARCHAR(50) NOT NULL ,
  station BOOLEAN NOT NULL ,
  name VARCHAR(50) NOT NULL ,
  address VARCHAR(200) NOT NULL ,
  passenger BOOLEAN NOT NULL ,
  luggage BOOLEAN NOT NULL ,
  package BOOLEAN NOT NULL ,
  PRIMARY KEY (bureau, station, name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


# stationcode
CREATE TABLE stationcode (
  name VARCHAR(10) NOT NULL ,
  code VARCHAR(10) NOT NULL ,
  PRIMARY KEY (code, name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;