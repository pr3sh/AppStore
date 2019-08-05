# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppStoreItem(scrapy.Item):
   


    name = scrapy.Field()
    # seller  = scrapy.Field()
    size = scrapy.Field()
    category = scrapy.Field()
    compatibility= scrapy.Field()
    languages = scrapy.Field()  
    age_rating = scrapy.Field()
    price = scrapy.Field()
    app_rating = scrapy.Field()    
    rating_count = scrapy.Field()
    rank = scrapy.Field()  
    rating_count = scrapy.Field()




