# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector, Selector
from scrapy.http.request import Request
from scrapy.http.cookies import CookieJar
from scrapy import FormRequest

'''
class ChouTiSpider(scrapy.Spider):
    # 爬虫应用的名称，通过此名称启动爬虫命令
    name = "chouti"
    # 允许的域名
    allowed_domains = ["chouti.com"]

    cookie_dict = {}
    has_request_set = {}

    def start_requests(self):
        url = 'http://dig.chouti.com/'
        # return [Request(url=url, callback=self.login)]
        yield Request(url=url, callback=self.login)

    def login(self, response):
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response, response.request)
        for k, v in cookie_jar._cookies.items():
            for i, j in v.items():
                for m, n in j.items():
                    self.cookie_dict[m] = n.value

        req = Request(
            url='http://dig.chouti.com/login',
            method='POST',
            headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            body='phone=8615131255089&password=pppppppp&oneMonth=1',
            cookies=self.cookie_dict,
            callback=self.check_login
        )
        yield req

    def check_login(self, response):
        req = Request(
            url='http://dig.chouti.com/',
            method='GET',
            callback=self.show,
            cookies=self.cookie_dict,
            dont_filter=True
        )
        yield req

    def show(self, response):
        # print(response)
        hxs = HtmlXPathSelector(response)
        news_list = hxs.select('//div[@id="content-list"]/div[@class="item"]')
        for new in news_list:
            # temp = new.xpath('div/div[@class="part2"]/@share-linkid').extract()
            link_id = new.xpath('*/div[@class="part2"]/@share-linkid').extract_first()
            yield Request(
                url='http://dig.chouti.com/link/vote?linksId=%s' %(link_id,),
                method='POST',
                cookies=self.cookie_dict,
                callback=self.do_favor
            )

        page_list = hxs.select('//div[@id="dig_lcpage"]//a[re:test(@href, "/all/hot/recent/\d+")]/@href').extract()
        for page in page_list:

            page_url = 'http://dig.chouti.com%s' % page
            import hashlib
            hash = hashlib.md5()
            hash.update(bytes(page_url,encoding='utf-8'))
            key = hash.hexdigest()
            if key in self.has_request_set:
                pass
            else:
                self.has_request_set[key] = page_url
                yield Request(
                    url=page_url,
                    method='GET',
                    callback=self.show
                )

    def do_favor(self, response):
        print(response.text)
'''


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://chouti.com/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True, callback=self.parse1)

    def parse1(self, response):
        """获取首页登录"""
        # response.text 首页所有内容
        from scrapy.http.cookies import CookieJar
        cookie_jar = CookieJar()
        self.cookie_jar = cookie_jar.extract_cookies(response, response.request)  # 获取响应中的cookies

        post_dict = {
            'phone': '8617748232617',
            'password': 'password',
            'oneMonth': 1,
        }

        import urllib.parse
        data = urllib.parse.urlencode(post_dict)    # urlencode转换为：phone=86123&password=123&oneMonth=1这种格式
        # 发送post请求准备登录
        yield Request(
            url='http://dig.chouti.com/login',
            method='POST',
            cookies=self.cookie_jar,
            body=data,
            headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            callback=self.parse2
        )

    def parse2(self, response):
        """response返回登录结果"""
        print(response.text)
        #  获取新闻列表
        yield Request(url='http://dig.chouti.com', cookies=self.cookie_jar, callback=self.parse3)

    def parse3(self, response):
        """点赞"""
        hxs = Selector(response)
        linkid_list = hxs.xpath('//div[@class="news-pic"]/img/@lang').extract()
        print(linkid_list)
        for link_id in linkid_list:
            # 获取每一个id去点赞
            base_url = "https://dig.chouti.com/link/vote?linksId={0}".format(link_id)
            yield Request(url=base_url, method='POST', cookies=self.cookie_jar, callback=self.parse4)

        # hxs.xpath('//div[@id="dig_lcpage"]//a/@href')
        # 寻找所有分页页面
        page_list = hxs.xpath('//a[@class="ct_pagepa"] /@href').extract()
        """https://dig.chouti.com/all/hot/recent/2"""
        for page in page_list:
            page_url = "https://dig.chouti.com%s" % page
            yield Request(url=page_url, method='GET', cookies=self.cookie_jar, callback=self.parse3)

    def parse4(self, responese):
        # 输出点赞结果
        print(responese.text)


