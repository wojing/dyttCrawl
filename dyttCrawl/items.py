# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyttcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    film_name= scrapy.Field()
    publish_time = scrapy.Field()
    full_name = scrapy.Field()
    trans_name = scrapy.Field()
    english_name = scrapy.Field()
    decade = scrapy.Field()
    country = scrapy.Field()
    film_type = scrapy.Field()
    language = scrapy.Field()
    subtitles = scrapy.Field()
    IMDB_score = scrapy.Field()
    douban_score = scrapy.Field()
    publish = scrapy.Field()
    director = scrapy.Field()
    format = scrapy.Field()
    resolution = scrapy.Field()
    size = scrapy.Field()
    duration = scrapy.Field()
    actor = scrapy.Field()
    magnet_link = scrapy.Field()
    thunder_link = scrapy.Field()
    image_link = scrapy.Field()
    introduction = scrapy.Field()


