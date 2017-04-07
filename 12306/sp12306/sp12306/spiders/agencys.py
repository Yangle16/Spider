#-*- coding:utf-8 -*-
import scrapy
import json, urllib

from ..items import AgencyItem, CommitItem
from scrapy.http.request import Request

class AgencysSpider(scrapy.Spider):
    name = 'agencys'
    start_urls = ['https://kyfw.12306.cn/otn/userCommon/allProvince']

    custom_settings = {
        'ITEM_PIPELINES':{
            'sp12306.pipelines.AgencySQLPipeline': 300,
        }
    }

    def parse(self, response):
        url = 'https://kyfw.12306.cn/otn/queryAgencySellTicket/query?'
        j = json.loads(response.body)

        for prov in j['data']:
            params = {'province':prov['chineseName'].encode('utf-8'), 'city':'', 'county':''}
            s_url = url + urllib.urlencode(params)
            yield Request(s_url, callback=self.parse_agency)

    def parse_agency(self, response):
        datas = json.loads(response.body)
        for data in datas['data']['datas']:
            item = AgencyItem()
            item['province'] = data['province'].encode('utf-8')
            item['city'] = data['city'].encode('utf-8')
            item['county'] = data['county'].encode('utf-8')
            item['address'] = data['address'].encode('utf-8')
            item['name'] = data['agency_name'].encode('utf-8')
            item['windows'] = data['windows_quantity'].encode('utf-8')
            item['start'] = data['start_time_am'].encode('utf-8')
            item['end'] = data['stop_time_pm'].encode('utf-8')
            yield item
        yield CommitItem()















