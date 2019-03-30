# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PattersonschwartzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ListingItem(scrapy.Item):
    price = scrapy.Field()
    cdp = scrapy.Field()
    address = scrapy.Field()
    fulladdress = scrapy.Field()
    description = scrapy.Field()
    listing = scrapy.Field()
    primarydetails = scrapy.Field()
