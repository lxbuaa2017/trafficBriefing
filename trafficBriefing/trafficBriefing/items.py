# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrafficbriefingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_urls = scrapy.Field()
    images = scrapy.Field()

    influence_snow = scrapy.Field()
    influence_fog = scrapy.Field()
    influence_thunder = scrapy.Field()
    pass
