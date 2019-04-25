
"""
@author: ejazshaikh
email : ejazshaikh94@yahoo.in
"""


import scrapy
import re
from ImdbScraper.items import MovieItem


class tutorialSpider(scrapy.Spider):
    name = "imdb"
     
    # my_url takes the url passed via command line 
    def __init__(self, my_url='', *args, **kwargs):
        super(tutorialSpider, self).__init__(*args, **kwargs)
        self.start_urls = [my_url]



    def parse(self, response):
        for sel in response.xpath("//*[contains(@class,'review-container')]"):
            item = MovieItem()
            item['review'] = sel.xpath('div/div[3]/div[1]/text()').extract()
            item['Rating'] = sel.xpath('div/div/span/span[1]/text()').extract()
            yield item

        #When we press the 'load more' button, an ajax request is generated.
        #From that request 'pagination key' is extracted and stored in data_key
        data_key = response.css('div.load-more-data::attr(data-key)').get()
        url = self.start_urls
        movie_key = response.url.split('/')[4]
        url = "https://www.imdb.com/title/"+str(movie_key)+"/reviews/_ajax?ref_=undefined&paginationKey="+str(data_key)
        next_page = url
        
        while(next_page is not None and data_key is not None):
        	data_key = response.css('div.load-more-data::attr(data-key)').get()
        	url = "https://www.imdb.com/title/"+str(movie_key)+"/reviews/_ajax?ref_=undefined&paginationKey="+str(data_key)
        	yield response.follow(next_page, callback=self.parse)

          	


	

    

















            