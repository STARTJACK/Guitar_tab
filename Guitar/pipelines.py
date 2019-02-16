# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

from urllib.parse import urlparse
from os.path import basename,dirname,join
import scrapy

class GuitarPipeline(object):
    def process_item(self, item, spider):
        return item

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(url=image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        path=urlparse(request.url).path
        return  (item['name'],basename(path))
