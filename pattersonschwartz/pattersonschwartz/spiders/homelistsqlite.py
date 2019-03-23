# -*- coding: utf-8 -*-
import scrapy
import json


class HomelistsqliteSpider(scrapy.Spider):
    name = 'homelistsqlite'
    allowed_domains = ['pattersonschwartz.com']
    page = 1
    api_url = 'http://www.pattersonschwartz.com/api/ps/forsale/Harford/priceMin_350000/priceMax_400000/page_{}'
    start_urls = [api_url.format(page)]

    custom_settings = {
        'ITEM_PIPELINES': {
            'pattersonschwartz.pipelines.PattersonschwartzPipeline' : 300
        }
    }

    def parse(self, response):
        data = json.loads(response.text)
        for r in data['thumbs']:
            yield{
                'id' : r['id'],
                'address' : r['a'],
                'price' : r['p'],
                'cdp' : r['c'],
            }
        if not data['isLastPage']:
            self.page += 1
            yield scrapy.Request(url=self.api_url.format(self.page), callback=self.parse)
