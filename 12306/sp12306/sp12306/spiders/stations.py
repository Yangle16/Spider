#-*- coding:utf-8 -*-
import scrapy
import json, urllib

from ..items import StationItem, CommitItem
from scrapy.http.request import Request

class StationsSpider(scrapy.Spider):
    name = 'stations'
    start_urls = ['http://www.12306.cn/mormhweb/kyyyz/']

    custom_settings = {
        'ITEM_PIPELINES':{
            'sp12306.pipelines.StationSQLPipeline': 300,
        }
    }

    def parse(self, response):
        names = response.css("#secTable > tbody > tr > td::text").extract()
        sub_urls = response.css("#mainTable td.submenu_bg > a::attr(href)").extract()
        for i in range(0, len(names)):
            sub_url1 = response.url + sub_urls[i * 2][2:]
            yield Request(sub_url1, callback=self.parse_station, meta={'bureau':names[i], 'station':True})

            sub_url2 = response.url + sub_urls[i * 2 + 1][2:]
            yield Request(sub_url2, callback=self.parse_station, meta={'bureau': names[i], 'station': False})

    def parse_station(self, response):
        datas = response.css("table table tr")
        if len(datas) <= 2:
            return
        for i in range(0, len(datas)):
            if i < 2:
                continue
            infos = datas[i].css("td::text").extract()

            item = StationItem()
            item['bureau'] = response.meta['bureau'].encode('utf-8')
            item['station'] = response.meta['station']
            item['name'] = infos[0].encode('utf-8')
            item['address'] = infos[1].encode('utf-8')
            item['passenger'] = infos[2].strip() != ''
            item['luggage'] = infos[3].strip() != ''
            item['package'] = infos[4].strip() != ''

            yield item
            print item
        yield CommitItem()















