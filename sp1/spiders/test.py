#!/usr/bin/env python
# -*- coding:utf-8 -*-
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import HtmlResponse


html = """<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <ul>
            <li class="item-"><a id='i1' href="link.html">first item</a></li>
            <li class="item-0"><a id='i2' href="llink.html">first item</a></li>
            <li class="item-1"><a href="llink2.html">second item<span>vv</span></a></li>
        </ul>
        <div><a href="llink2.html">second item</a></div>
    </body>
</html>
"""
'''

response = HtmlResponse(url='http://example.com', body=html, encoding='utf-8')
hxs = HtmlXPathSelector(response)
print(hxs)
hxs = Selector(response=response).xpath('//a')      # 找html页面中全部a标签
for i in hxs:
    print(i)
print(hxs)

hxs = Selector(response=response).xpath('//a[1]') #
for i in hxs:
    print(i)
print(hxs)
print(hxs)

hxs = Selector(response=response).xpath('//a[@id]')     # 找具有id属性的a标签
print(hxs)

hxs = Selector(response=response).xpath('//a[@id="i1"]')   # 找具有id属性且值为i1的a标签
print(hxs)

hxs = Selector(response=response).xpath('//a[@href="link.html"][@id="i1"]') # href属性值为link.html且id属性且值为i1的a标签
print(hxs)

hxs = Selector(response=response).xpath('//a[contains(@href, "link2")]')     # contains函数：匹配一个属性值中包含的字符串，找出属性href值包含link2的a标签
print(hxs)

hxs = Selector(response=response).xpath('//a[starts-with(@href, "link")]')  # 属性href以link开头的a标签
print(hxs)

hxs = Selector(response=response).xpath('//a[re:test(@id, "i\d+")]')        # 正则匹配，id属性包含“i+数字”的a标签
print(hxs)
hxs = Selector(response=response).xpath('//a[re:test(@id, "i\d+")]/text()').extract()   # id属性包含“i+数字”的a标签的值
print(hxs)
hxs = Selector(response=response).xpath('//a[re:test(@id, "i\d+")]/@href').extract()  # id属性包含“i+数字”的a标签的href属性值
print(hxs)
hxs = Selector(response=response).xpath('/html/body/ul/li/a/@href').extract()           # 取/html/body/ul/li/a/路径下@href的值，多个值返回列表
print(hxs)
hxs = Selector(response=response).xpath('//body/ul/li/a/@href').extract_first()# 取/html/body/ul/li/a/路径下@href的第一个值
print(hxs)


#  相对路径的xpath
ul_list = Selector(response=response).xpath('//body/ul/li')
for item in ul_list:
    # v = item.xpath('./a/span')
    # 或
    # v = item.xpath('a/span')
    # 或
    v = item.xpath('*/a/span')
    print(v)
    
'''

# assert 1 == 2

class A(object):
    def foo1(self):
        print("Hello", self)

    @staticmethod
    def foo2():
        print("hello")

    @classmethod
    def foo3(clss):
        print("hello", clss)

A.foo3()