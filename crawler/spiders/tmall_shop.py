# -*- coding:utf-8 -*-
from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
from urllib2 import urlopen
from scrapy.conf import settings
import re
import time
import datetime
from crawler.items import DirbotItem
from socket import *

def get_now():
    ''' 得到当前时间 '''
    return datetime.datetime.now()

def get_id(url):
    ''' 得到淘宝商品ID '''
    for i in urlparse(url).query.split("&"):
        if "id=" in i:
            return i.replace("id=", "")
        else:
            return False

class DmozSpider(CrawlSpider):
    name = "shop"
    allowed_domains = ["tmall.com", "taobao.com"]
    start_urls = [
    "http://shouer123.taobao.com/search.htm",
        ]


    rules = (
        # 符合规则的网址, 只抓取链接
        # Rule(SgmlLinkExtractor(allow=(r'http://[\w]+.(taobao|tmall).com/search.htm?(.*)&pageNum=([0-9]+)(.*)'), deny=("&pv="))),
        Rule(SgmlLinkExtractor(allow=(r'http://(.+?).[taobao|tmall].com/search.htm\?(.*?)[&|;]pageNo=(\d+)(.*?)'), deny=("&pv="))),
        Rule(SgmlLinkExtractor(allow=(r'http://(.+?).[taobao|tmall].com/search.htm\?(.*?)[&|;]pageNum=(\d+)(.*?)'), deny=("&pv="))),

        # 符合规则的网址, 提取内容
        Rule(SgmlLinkExtractor(allow=(r'http://detail.tmall.com/item.htm\?(.*?)&?id=\d+&?')), callback="parse_item"),
        Rule(SgmlLinkExtractor(allow=(r'http://item.taobao.com/item.htm\?(.*?)&?id=\d+&?')), callback="parse_item"),
        Rule(SgmlLinkExtractor(allow=(r'http://detail.tmall.com/item.htm\?(.*?)&?id=\d+')), callback="parse_item"),
        Rule(SgmlLinkExtractor(allow=(r'http://item.taobao.com/item.htm\?(.*?)&?id=\d+')), callback="parse_item"),
        Rule(SgmlLinkExtractor(allow=(r'http://detail.tmall.com/item.htm\?spm=(.*?)&?id=\d+&?')), callback="parse_item"),
        Rule(SgmlLinkExtractor(allow=(r'http://item.taobao.com/item.htm\?spm=(.*?)&?id=\d+&?')), callback="parse_item"),
    )
            
    def parse_item(self, response):
        soup = BeautifulSoup(response.body_as_unicode())
        item = DirbotItem() 

        item['url'] = response.url
        
        ADDR = (settings["DAEMON_HOST"], settings["DAEMON_PORT"])
        BUFSIZE = 1024
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        if get_id(item['url']):
            item['product_id'] = get_id(item['url'])

            if 'tmall.com' in item['url']:
                item['platform'] = 'tmall'
            else:
                item['platform'] = 'taobao'
            
            data = "%s:%s" % (item["platform"], item["product_id"])
            print data
            
            tcpCliSock.send("%s\r\n" % data)
            data = tcpCliSock.recv(BUFSIZE)
            print data.strip()
            time.sleep(3)

            return item
        tcpCliSock.close()

