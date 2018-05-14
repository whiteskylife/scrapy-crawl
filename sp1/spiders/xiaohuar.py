# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    # allowed_domains = ['gxyclub.com']
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    def parse(self, response):
        # 要废弃
        # hxs = HtmlXPathSelector(response)
        # print(hxs)
        # result = hxs.select('//a[@class="item_list"]')

        hxs = Selector(response=response)
        # obj = hxs.xpath('//div[@class="invest-inner"]')
        # obj = hxs.xpath('//*[@id="newsContent19494036"]/div[3]/a[1]/i').extract()
        obj = hxs.xpath('//div[@class="part2"]/@share-linkid').extract()
        print(obj)
        # for item in obj:
        #     price = item.xpath('.//span[@class="price"]/text()').extract_first()
        #     url = item.xpath('div[@class="item_t"]/div[@class="class"]//a/@href').extract_first()

