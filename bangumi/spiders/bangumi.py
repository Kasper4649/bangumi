# -*- coding: utf-8 -*-
import scrapy
from bangumi.items import BangumiItem


class BangumiSpider(scrapy.Spider):
    name = 'bangumi'
    allowed_domains = ['bgm.tv']
    start_urls = []
    for i in range(1, 11):
        start_urls.append('https://bgm.tv/anime/browser?sort=rank&page=%s' % i)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        anime_list = response.xpath("//ul[@class='browserFull']//li")

        for anime in anime_list:
            _id = anime.xpath("@id").get().replace("item_", "")
            title = anime.xpath(".//h3//a/text()").get()
            kata_title = anime.xpath(".//small[@class='grey']/text()").get("")
            image = anime.xpath(".//img/@src").get().replace("//", "")
            link = "https://bgm.tv" + anime.xpath(".//a/@href").get()
            info = anime.xpath(".//p[@class='info tip']/text()").get().strip()
            rank = anime.xpath(".//span[@class='rank']/text()").get()
            rate = anime.xpath(".//small[@class='fade']/text()").get()

            item = BangumiItem(_id=_id, title=title, kata_title=kata_title, image=image, link=link, info=info,
                               rank=rank, rate=rate)

            yield item
