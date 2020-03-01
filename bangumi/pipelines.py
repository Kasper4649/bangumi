# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter


class BangumiPipeline(object):

    def __init__(self):
        self.fp = open("anime.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.fp.write(b"[")

    def open_spider(self, spider):
        self.exporter.start_exporting()
        print("开始爬取信息。")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        self.fp.write(b",")
        return item

    def close_spider(self, spider):
        self.fp.write(b"]")
        print("结束爬取信息。")
