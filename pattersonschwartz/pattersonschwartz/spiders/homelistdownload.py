# -*- coding: utf-8 -*-
import scrapy


class HomelistdownloadSpider(scrapy.Spider):
    name = 'homelistdownload'
    allowed_domains = ['pattersonschwartz.com']
    start_urls = ['http://www.pattersonschwartz.com/forsale/Harford/priceMin_300000/priceMax_400000/sort_1/']

    def parse(self, response):
        for r in response.css('.psr-result'):
            yield {
                'price': r.css('.psr-price::text').get(),
                'cdp': r.css('.psr-address > span:nth-of-type(1)::text').get(),
                'address': r.css('.psr-address > span:nth-of-type(2)::text').get(),
                'listingurl': r.css('.psr-more-info::attr(href)').get()
            }
