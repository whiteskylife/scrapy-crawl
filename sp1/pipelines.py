# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Sp2Pipeline(object):
    def __init__(self, val):
        self.val = val
        self.f = None

    def process_item(self, item, spider):
        """
        :param item:  爬虫中yield回来的对象
        :param spider: 爬虫对象 obj = JianDanSpider(); 有spider.name等属性
        """
        if spider.name == 'jiadnan':        # 由于pipeline是全局的，所有的spider执行时，只要yield过来item对象，都会执行pipeline，这里可以通过spider.name属性做判断，选择性的执行pipeline
            pass
        print(item)

        a = item['url'] + ' ' + item['text'] + '\n'
        self.f.write(a)
        # return item             # 将item传递给下一个pipeline的process_item方法，不写传递None，依然会执行
        # from scrapy.exceptions import DropItem
        # raise DropItem()          # DropItem:下一个pipeline的process_item方法不在执行

    @classmethod
    def from_crawler(cls, crawler):
        """
        用于实例化Sp2Pipeline对象，过程中可以通过crawler封装一些参数到对象中
        初始化时候，用于创建pipeline对象,classmethod装饰器会把cls替换为当前类
        :param crawler:有爬虫相关的参数封装，可以取配置文件中的值（settings定义的key必须大写）：crawler.settings.get('MMMM')
        :return:
        """
        print('执行pipeline的from_crawler方法，进行实例化对象')
        val = crawler.settings.get('MMMM')
        return cls(val)  # 实例化对象，并通过对象的__init__方法初始化val封装到对象中

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        self.f = open('a.log', 'a+', encoding='utf-8')
        print('打开爬虫')

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        self.f.close()
        print('关闭爬虫')


# class Sp3Pipeline(object):
#     def __init__(self):
#         self.f = None
#
#     def process_item(self, item, spider):
#         """
#
#         :param item:  爬虫中yield回来的对象
#         :param spider: 爬虫对象 obj = JianDanSpider()
#         :return:
#         """
#         print('in the pipeline3--------------------------')
#         return item
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         """
#         初始化时候，用于创建pipeline对象
#         :param crawler:
#         :return:
#         """
#         # val = crawler.settings.get('MMMM')
#         print('执行pipeline的from_crawler，进行实例化对象')
#         return cls()
#
#     def open_spider(self, spider):
#         """
#         爬虫开始执行时，调用
#         :param spider:
#         :return:
#         """
#         print('in the pipeline3-------------------------- 打开爬虫')
#         # self.f = open('a.log', 'a+')
#
#     def close_spider(self, spider):
#         """
#         爬虫关闭时，被调用
#         :param spider:
#         :return:
#         """
#         print('in the pipeline3-------------------------- 关闭爬虫')
