# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #在item里定义数据类型
    title = scrapy.Field()
    pic = scrapy.Field()
    pass
