# Imdb Review Scraper

*NOTES*

This spider is written in python using the Scrapy framework. Do with it what you will. If you'd like to contribute please contact me at ejazshaikh94@yahoo.in.

One thing to note if you do use this project, be aware that I'm not sure of the legality of this in a proffessinal setting, so use it at your own risk. Also be aware that you can get your ip address banned from websites if you scrap. There are ways of mitagating this risk such as adding delay between requests, which I've built into this by default, but nonetheless there is still risk.

To run this code you need to have Python 3 installed on your computer and you need to have Scrapy 1.6 installed

*WORKING*

Currently this program takes a title's imdb review page url as argument and scrapes all the reviews and user rating for that perticular movie. The title can be a movie, TV series, anime or anything. As long as it has an review page, its in the program's scope.

The reviews fetched are stored in mongodb database along with their corresponding user rating. For that you have to create a mongodb database and collection. Then pass the database name in the settings.py file and collection's name in pipeline.py file.

**STEPS TO RUN

1) Go to your parent directory. For example:
