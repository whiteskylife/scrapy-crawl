#!/usr/bin/env python
# -*-coding:utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector, Selector
from scrapy.http.request import Request


class JianDanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True, callback=self.parse1)

    def parse1(self, response):
        # print(response.text)
        hxs = Selector(response)
        a_list = hxs.xpath('//div[@class="indexs"]/h2')
        for tag in a_list:
            url = tag.xpath('./a/@href').extract_first()
            text = tag.xpath('./a/text()').extract_first()
            # print(url)
            # print(text)
            from ..items import Sp2Item
            yield Sp2Item(url=url, text=text)


