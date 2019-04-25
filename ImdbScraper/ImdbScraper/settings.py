# -*- coding: utf-8 -*-

# Scrapy settings for project


BOT_NAME = 'ImdbScraper'

SPIDER_MODULES = ['ImdbScraper.spiders']
NEWSPIDER_MODULE = 'ImdbScraper.spiders'



# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'ImdbScraper.pipelines.MongoPipeline': 300,
}
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'your database name'


