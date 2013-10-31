# -*- encoding: utf-8 -*-

DOWNLOAD_DELAY = 3  # The amount of time (in secs) that the downloader should wait before downloading consecutive pages from the same spider.
# DEPTH_LIMIT = 15 # The maximum depth that will be allowed to crawl for any site. If zero, no limit will be imposed.
# DEPTH_STATS = False # Whether to collect maximum depth stats.
# DOWNLOADER_STATS = False    # Whether to enable downloader stats collection.
DOWNLOAD_TIMEOUT = 250  # The amount of time (in secs) that the downloader will wait before timing out.

# LOG_ENABLED = False # Whether to enable logging.
# LOG_LEVEL = "INFO"    # Minimum level to log. Available levels are: CRITICAL, ERROR, WARNING, INFO, DEBUG.

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
DEFAULT_ITEM_CLASS = 'crawler.items.DirbotItem'

# ITEM_PIPELINES = ['crawler.pipelines.MySQLStorePipeline']
# ITEM_PIPELINES = ['crawler.pipelines.MongoStorePipeline']

MYSQL_HOST = 'host'
MYSQL_PORT = 3306
MYSQL_DB = 'database'
MYSQL_USER = 'dbuser'
MYSQL_PASSWD = 'dbpasswd'
MYSQL_CHARSET = 'utf8'

MONGO_HOST = 'mongohost'
MONGO_PORT = 27017
MONGO_DB = 'mongbdb'
MONGO_COLLECTION = 'mongocollection'

DAEMON_HOST = "daemonhost"
DAEMON_PORT = 19999
USER_AGENT = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"
