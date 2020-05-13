# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['buy.cars45.com']
    start_urls = ['https://buy.cars45.com']

    def parse(self, response):
        pass
