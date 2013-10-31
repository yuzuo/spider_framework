# -*- encoding: utf-8 -*-
from scrapy.item import Item, Field

class DirbotItem(Item):
    platform = Field()  # 平台: taobao, tmall, etc..
    url = Field()   # 商品URL
    product_id = Field() # 淘宝商品ID
    create_time = Field()   # 抓取时间

class Website(DirbotItem):
    url = Field()
    def __str__(self):
        return "Website: name=%s url=%s" % (self.get('name'), self.get('url'))
