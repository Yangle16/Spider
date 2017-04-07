# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Sp12306Pipeline(object):
    def process_item(self, item, spider):
        return item


import pymysql.cursors

from scrapy.exceptions import DropItem
from items import CommitItem

class ProvincePipeline2(object):
    def process_item(self, item, spider):
        print item['name'], '------'
        return item

class ProvincePipeline1(object):
    def process_item(self, item, spider):
        if item['name']:
            return item
        else:
            raise DropItem("None item")

class AgencySQLPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            self.conn = pymysql.connect(
                host="localhost",
                port=3306,
                user='root',
                password='2008512lele',
                db='12306_train',
                charset='utf8'
            )
            self.conn.set_character_set('utf8')
            self.cursor = self.conn.cursor()
            self.cursor.execute('SET NAMES utf8;')
            self.cursor.execute('SET CHARACTER SET utf8;')
            self.cursor.execute('SET character_set_connection=utf8;')
            self.conn.commit()
        else:
            self.cursor = self.conn.cursor()
            self.sql = "insert into agencys VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
            self.cursor.execute(self.sql,(item['province'],item['city'], item['county'],item['address'],item['name'],item['windows'],item['start'],item['end']))

            self.conn.commit()



class StationSQLPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            self.conn = pymysql.connect(
                host="localhost",
                port=3306,
                user='root',
                password='2008512lele',
                db='12306_train',
                charset='utf8'
            )
            self.conn.set_character_set('utf8')
            self.cursor = self.conn.cursor()
            self.cursor.execute('SET NAMES utf8;')
            self.cursor.execute('SET CHARACTER SET utf8;')
            self.cursor.execute('SET character_set_connection=utf8;')
            self.conn.commit()
        else:
            self.cursor = self.conn.cursor()
            self.sql = "insert into stations VALUES (%s,%s,%s,%s,%s,%s,%s);"
            self.cursor.execute(self.sql,(item['bureau'],item['station'], item['name'],item['address'],item['passenger'],item['luggage'],item['package']))

            self.conn.commit()


class StationCodeSQLPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CommitItem):
            self.conn = pymysql.connect(
                host="localhost",
                port=3306,
                user='root',
                password='2008512lele',
                db='12306_train',
                charset='utf8'
            )
            self.conn.commit()
        else:
            self.conn = pymysql.connect(
                host="localhost",
                port=3306,
                user='root',
                password='2008512lele',
                db='12306_train',
                charset='utf8'
            )
            self.cursor = self.conn.cursor()
            self.sql = "insert into stationcode VALUES (%s,%s);"
            self.cursor.execute(self.sql,(item['name'],item['code']))

            self.conn.commit()















