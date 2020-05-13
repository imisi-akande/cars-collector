# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['buy.cars45.com']
    start_urls = ['https://buy.cars45.com']

    def parse(self, response):
        categories = response.xpath('//*[@class="landing_featured_box"]/a/@href').extract()
        for category in categories:
            yield Request(category, callback=self.parse_categories)
 
    def parse_categories(self, response):
        # open_in_browser(response)
        # inspect_response(response, self)
 
        new_cars = response.xpath('//div[@class="product_box"]')
        for new_car in new_cars:
            model = new_car.xpath('.//h4/text()').extract_first().strip()
            status = new_car.xpath('.//p/text()').extract_first()
            price = new_car.xpath('.//h5[@class="price"]/text()').extract_first().strip()
            mileage = new_car.xpath('.//span[text()="Mileage:"]/following-sibling::span/text()').extract_first()
            year = new_car.xpath('.//span[text()="Year:"]/following-sibling::span/text()').extract_first()
 
            try:
                year = re.findall('\d{4}', model)[0]
            except:
                year = ''
 
            car_id = ''
 
            yield{"model": model,
                    "status": status,
                    "price": price,
                    "mileage": mileage,
                    "year": year,
                    "car_id": car_id}
 
        next_pages = response.xpath('//a[@class="page-link"]/@href').extract()
        for next_page in next_pages:
            print(next_page, 'next')
            if next_page != "javascript:;":
                yield Request(next_page, callback=self.parse_categories)