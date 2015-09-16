# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy import Field,Item

class DoubanmovieItem(Item):
    title = Field()
    movieInfo = Field()
    star = Field()
    quote = Field()
