#-*- coding:utf-8 -*-
import scrapy
import json

from ..items import ProvincesItem

class ProvincesSpider(scrapy.Spider):
    name = 'provinces'
    start_urls = ['https://kyfw.12306.cn/otn/userCommon/allProvince']

    custom_settings = {
        'ITEM_PIPELINES':{
            'sp12306.pipelines.ProvincePipeline1': 300,
            'sp12306.pipelines.ProvincePipeline2': 400,
        }
    }

    def parse(self, response):
        j = json.loads(response.body)

        for prov in j['data']:
            item = ProvincesItem()
            item['name'] = prov['chineseName']
            yield item
        item = ProvincesItem()
        item['name'] = None
        yield item