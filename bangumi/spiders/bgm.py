# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BgmSpider(CrawlSpider):
    name = 'bgm'
    allowed_domains = ['bgm.tv']
    start_urls = ["https://bgm.tv/book/browser?sort=rank&page=1"]

    rules = (
        Rule(LinkExtractor(allow=r'.+sort=rank&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
