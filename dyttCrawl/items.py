# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyttcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name= scrapy.Field()
    publish_time = scrapy.Field()
    full_name = scrapy.Field()
    translate_name = scrapy.Field()
    english_name = scrapy.Field()
    publish_year = scrapy.Field()
    production_place = scrapy.Field()
    film_type = scrapy.Field()
    language = scrapy.Field()
    subtitle = scrapy.Field()
    imba_score = scrapy.Field()
    douban_score = scrapy.Field()
    director = scrapy.Field()
    magnet_link = scrapy.Field()
    thunder_link = scrapy.Field()
    image_link = scrapy.Field()
    introduction = scrapy.Field()

