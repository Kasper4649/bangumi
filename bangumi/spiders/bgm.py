# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BgmSpider(CrawlSpider):
    name = 'bgm'
    allowed_domains = ['bgm.tv']
    start_urls = ["https://bgm.tv/music/browser?sort=rank&page=1"]

    rules = (
        Rule(LinkExtractor(allow=r'&page=\d+')),
        Rule(LinkExtractor(allow=r'https://bgm.tv/subject/\d+'), callback='parse_detail'),
    )

    def parse_detail(self, response):
        item = {}
        item['id'] = response.xpath('//h1[@class="nameSingle"]/a/@href').get().replace("/subject/", "")
        item['name'] = response.xpath('//h1[@class="nameSingle"]/a/text()').get()
        # 下同省略
        return item
