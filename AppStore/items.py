# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppstoreItem(scrapy.Item):
   


    Names = scrapy.Field()
    Provider  = scrapy.Field()
    Size = scrapy.Field()
    Category = scrapy.Field()
    Compatibility= scrapy.Field()
    Languages = scrapy.Field()  
    Age_Rating = scrapy.Field()
    Price = scrapy.Field()
    App_Rating = scrapy.Field()    




