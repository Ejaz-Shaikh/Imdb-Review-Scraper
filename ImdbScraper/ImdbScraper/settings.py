# -*- coding: utf-8 -*-

# Scrapy settings for project


BOT_NAME = 'ImdbScraper'

SPIDER_MODULES = ['ImdbScraper.spiders']
NEWSPIDER_MODULE = 'ImdbScraper.spiders'


#Configure maximum concurrent requests performed by Scrapy (default: 16)
#You can remove this if the wbsite you are scraping dosen't put restrictions on scraping frequency
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'ImdbScraper.pipelines.MongoPipeline': 300,
}
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'your database name'


