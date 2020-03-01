# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BangumiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    title = scrapy.Field()
    kata_title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    info = scrapy.Field()
    rank = scrapy.Field()
    rate = scrapy.Field()

