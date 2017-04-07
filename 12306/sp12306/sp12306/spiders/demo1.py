#-*- coding:utf-8 -*-
import scrapy

class FirstSpider(scrapy.Spider):
    name = 'python'
    start_urls = ['http://cuiqingcai.com/category/technique/python']

    def parse(self, response):
        print '--' * 50
        print response.url
        print response.headers
        print response.body