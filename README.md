# Imdb Review Scraper

## *NOTES*

This spider is written in python using the Scrapy framework. Do with it what you will. If you'd like to contribute please contact me at ejazshaikh94@yahoo.in.

One thing to note if you do use this project, be aware that I'm not sure of the legality of this in a professional setting, so use it at your own risk. Also be aware that you can get your ip address banned from websites if you scrape. There are ways of mitagating this risk such as adding delay between requests, which I've built into this by default, but nonetheless there is still risk.

To run this code you need to have Python 3 installed on your computer along with have Scrapy 1.6 or greater.

## *WORKING*

Currently this program takes a title's imdb review page url as argument and scrapes all the reviews and user rating for that perticular movie. The title can be a movie, TV series, anime or anything. As long as it has an review page, its in the program's scope.

The reviews fetched are stored in mongodb database along with their corresponding user rating. For that you have to create a mongodb database and collection. Then pass the database name in the settings.py file and collection's name in pipeline.py file.

## *STEPS TO RUN*

1. Go to your parent directory. For example:

   ![im1](https://user-images.githubusercontent.com/34889668/56755431-23415c80-67ad-11e9-8f65-d62b245a8ab5.png)

   Type: cd {your parent directory path}


2. To run the script type:
   scrapy crawl imdb -a my_url = "{the title's url}"
   
   For example consider we want to scrape review for movie "Badla"
   The url for its review page would be: https://www.imdb.com/title/tt8130968/reviews?ref_=tt_urv
   
   ![im2](https://user-images.githubusercontent.com/34889668/56755816-fd688780-67ad-11e9-8321-e361eddee812.png)
   So the command for this would be : 
   scrapy crawl imdb -a my_url = "https://www.imdb.com/title/tt8130968/reviews?ref_=tt_urv"
   
   
3. Open the mongodb database collection in which you have chosen to save the data. Its been assumed here that you have            already created an database and collection and passed their names to settings.py and pipelines.py files respectively.  
   
   
4. And with that you have fetched all the reviews for your desired title. Whether it be a movie, tv or anime. :smile:   
