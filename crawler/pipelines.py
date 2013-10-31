# -*- encoding: utf-8 -*-

# from scrapy import log
from scrapy.http import Request
from scrapy.conf import settings
from pymongo import Connection
import MySQLdb

class MySQLStorePipeline(object):
    def __init__(self):
        host = settings['MYSQL_HOST']
        db = settings['MYSQL_DB']
        port = settings['MYSQL_PORT']
        user = settings['MYSQL_USER']
        passwd = settings['MYSQL_PASSWD']
        charset = settings['MYSQL_CHARSET']
        
        self.conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        query = '''
        INSERT INTO crawl_product(product_id, tb_user_id, url, comments, platform, sold_num, create_time)
        VALUES ("%s", "%s", "%s", '%s', "%s", %s, "%s")
        ''' % (item['product_id'], item['tb_user_id'], item['url'], item['comments'], item['platform'], item['sold_num'], item['create_time'])
        self.cursor.execute(query)
        self.conn.commit()

        return item

class MongoStorePipeline(object):
    def __init__(self):
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        db = settings['MONGO_DB']
        collection = settings['MONGO_COLLECTION']
        self.connection = Connection(host, port)
        self.db = self.connection[db]
        self.collection = self.db[collection]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
            
        return item
