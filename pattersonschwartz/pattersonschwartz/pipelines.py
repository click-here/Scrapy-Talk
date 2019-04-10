# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import os
from scrapy.utils.conf import closest_scrapy_cfg
import datetime
import re


proj_root = os.path.dirname(closest_scrapy_cfg())

sqlite_file = os.path.join(proj_root, 'homes.db')

class PattersonschwartzPipeline(object):
    # requires a sqlite table like this:
    # CREATE TABLE "Homes" ( `address` TEXT, `listingid` TEXT, `cdp` TEXT, `createdon` TEXT, `currentprice` INTEGER )
    def __init__(self):
        self.conn = sqlite3.connect(sqlite_file)
        self.c = self.conn.cursor()


    def process_item(self, item, spider):
        currentprice = ''.join(re.findall('\d+', item['price']))
        self.c.execute('insert into Homes values (?,?,?,?,?)', (item['address'], item['id'], item['cdp'], datetime.datetime.now(), currentprice))
        self.conn.commit()
        return item

    