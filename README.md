# IMDb Review Scraper

## NOTES

This spider is written in python using the Scrapy framework. Do with it what you will. If you'd like to contribute please contact me at ejazshaikh94@yahoo.in.

One thing to note if you do use this project, be aware that I'm not sure of the legality of this in a professional setting, so use it at your own risk. Also be aware that you can get your IP address banned from websites if you scrape. There are ways of mitigating this risk by adding delay between requests, which I've built into this by default, but nonetheless there is still risk.


## Dependencies
- Python3 +
- Scrappy1.6 +

## WORKING

A user inputs a movie name (by movie name I mean to include everything on IMDb as long as it has some reviews)

The reviews and ratings are fetched and stored in the MongoDB database (For which you'll need to create a MongoDB database and collection). Then pass the database name in the settings.py file and collection's name in pipeline.py file.

The collected data is shown in a proper format to the user.

## STEPS TO RUN

1. Navigate to your parent directory using terminal command `cd`.

   ![im1](https://user-images.githubusercontent.com/34889668/56755431-23415c80-67ad-11e9-8f65-d62b245a8ab5.png)

   Type: `cd {your parent directory path}`
   
   eg. `cd Desktop/my_directory`


2. To run the script type:
   
   `scrapy crawl imdb -a my_url = "{the title's url}"`
   
   For example :  if we want to scrape review for a movie called "Badla"
   The URL for its review page would be: `https://www.imdb.com/title/tt8130968/reviews?ref_=tt_urv`
   
   ![im2](https://user-images.githubusercontent.com/34889668/56755816-fd688780-67ad-11e9-8321-e361eddee812.png)
   So the command for this would be : 
   `scrapy crawl imdb -a my_url = "https://www.imdb.com/title/tt8130968/reviews?ref_=tt_urv"`
   
   
3. Open the MongoDB database collection in which you have chosen to save the data. At this point you should already have a database and collection and links to those in setting.py and pipeline.py respectively.
   
   
4. Now sit back and let the spider crawl :smile:

## Contributions:
[Husain Shaikh](GitHub.com/HusainShaikh895)
