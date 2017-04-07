#-*- coding:utf-8 -*-
import scrapy
import json, urllib

from ..items import StationCodeItem, CommitItem
from scrapy.http.request import Request

class StationCodeSpider(scrapy.Spider):
    name = 'stationcode'
    start_urls = ['https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9001']

    custom_settings = {
        'ITEM_PIPELINES':{
            'sp12306.pipelines.StationCodeSQLPipeline': 300,
        }
    }

    def parse(self, response):
        datas = response.body.decode('utf-8')
        stations = datas.split('@')

        for i in range(1, len(stations)):
            station = stations[i].split('|')

            item = StationCodeItem()
            item['name'] = station[1]
            item['code'] = station[2]
            yield item

        yield CommitItem()

