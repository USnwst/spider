import scrapy
from test1.items import Test1Item

class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']

    def parse(self, response):
        #图片地址//a[@class='u-card']/img/@data-src
        #文字地址//a[@class='u-card']/img/@alt
        datas_pic = response.xpath("//div[@class='slist']/ul/li/a/img")

        for item in datas_pic:

            #使用items存储
            pic=item.xpath("@src").extract()
            title = item.xpath("@alt").extract()
            topipeline1 = Test1Item(pic=pic,title=title)
            yield topipeline1
        pass