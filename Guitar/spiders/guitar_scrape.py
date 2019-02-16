# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import GuitarItem

class GuitarScrapeSpider(scrapy.Spider):
    name = 'guitar_scrape'
    allowed_domains = ['yinyuesheng.cn']
    start_urls = ['http://www.yinyuesheng.cn/jita/zhitan/']

    def parse(self, response):
        #提取当前页面所有链接
        le=LinkExtractor(restrict_css="ul.searchlist>li")
        links=le.extract_links(response)
        for link in links:
            yield scrapy.Request(url=link.url,callback=self.parse_image)
        #提取下一页
        le=LinkExtractor(restrict_css='div#pages > a')
        next=le.extract_links(response)[-1]
        if next.text=="下一页":
            yield scrapy.Request(url=next.url,callback=self.parse)

    def parse_image(self, response):
         links=response.xpath('//*[@id="Article"]/ul[1]/li/a/@href').extract()
         name=response.xpath('/html/body/div[4]/div[1]/div[1]/div[2]/h1/text()').extract()[0]
         item=GuitarItem()
         item['image_urls']=links
         item['name']=name
         yield item