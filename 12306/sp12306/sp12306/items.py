# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Sp12306Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProvincesItem(scrapy.Item):
    name = scrapy.Field()

class AgencyItem(scrapy.Item):
    province = scrapy.Field()
    city = scrapy.Field()
    county = scrapy.Field()
    address = scrapy.Field()
    name = scrapy.Field()
    windows = scrapy.Field()
    start = scrapy.Field()
    end = scrapy.Field()

class StationItem(scrapy.Item):
    bureau = scrapy.Field()
    station = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    passenger = scrapy.Field()
    luggage = scrapy.Field()
    package = scrapy.Field()

class StationCodeItem(scrapy.Item):
    name = scrapy.Field()
    code = scrapy.Field()

class CommitItem(scrapy.Item):
    pass



