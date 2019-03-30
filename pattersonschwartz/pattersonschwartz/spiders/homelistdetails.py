# -*- coding: utf-8 -*-
import scrapy
from pattersonschwartz.items import ListingItem


class HomelistdetailsSpider(scrapy.Spider):
    name = 'homelistdetails'
    allowed_domains = ['pattersonschwartz.com']
    start_urls = ['http://www.pattersonschwartz.com/forsale/Harford/priceMin_250000/priceMax_650000']

    def parse(self, response):
        for r in response.css('.psr-result'):
            listingurl = r.css('.psr-more-info::attr(href)').get()

            item = ListingItem()
            item['price'] = r.css('.psr-price::text').get()
            item['cdp'] = r.css('.psr-address > span:nth-of-type(1)::text').get()
            item['address'] = r.css('.psr-address > span:nth-of-type(2)::text').get()
            item['listing'] = listingurl

            request = scrapy.Request(url=response.urljoin(listingurl), callback=self.parse_details)
            request.meta['item'] = item
            yield request

    def get_primary_details(self, details):
        all_strongs = details.xpath('.//strong/text()').getall()
        detail_dict = {}
        for s in all_strongs:
            value = details.xpath('//strong[text()=$val]/following-sibling::text()', val=s).get()
            cleaned_strong = s.replace(':','')
            detail_dict[cleaned_strong] = value.strip()
        return detail_dict

    def parse_details(self, response):
        item = response.meta['item']
        item['fulladdress'] = response.css('.property-location::text').get().strip()
        item['description'] = response.xpath('.//*[@class="secondary-details"]/div/div/p/text()').get()
        item['primarydetails'] = self.get_primary_details(response.css('.primary-details'))

        yield item
