from scrapy import signals


# 1、在与settings同级目录下新建一个文件，文件名可以为extentions.py,内容如下
class MyExtension(object):
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_crawler(cls, crawler):
        val = crawler.settings.getint('MMMM')
        ext = cls(val)
        print('in the signals=================================')
        # crawler.signals.connect： 在scrapy中注册信号
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)

        return ext

    def spider_opened(self, spider):
        print('signals==========================open')

    def spider_closed(self, spider):
        print('signals==========================close')

# 配置生效
# EXTENSIONS = {
#     'sp1.extensions.MyExtension': 200,
# }
