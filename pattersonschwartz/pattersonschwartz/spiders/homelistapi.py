# -*- coding: utf-8 -*-
import scrapy
import json

class HomelistapiSpider(scrapy.Spider):
    name = 'homelistapi'
    allowed_domains = ['pattersonschwartz.com']
    page = 1
    api_url = 'http://www.pattersonschwartz.com/api/ps/forsale/Cecil,Harford/priceMin_525000/priceMax_600000/page_{}'
    start_urls = [api_url.format(page)]

    def parse(self, response):
        data = json.loads(response.text)
        for r in data['thumbs']:
            yield {
                'id' : r['id'],
                'address' : r['a'],
                'price' : r['p'],
                'cdp' : r['c'],
                'picture' : r['pu']
            }
        if not data['isLastPage']:
            self.page += 1
            yield scrapy.Request(url=self.api_url.format(self.page), callback=self.parse)

