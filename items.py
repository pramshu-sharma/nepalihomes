# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapperOneItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class PropertyItem(scrapy.Item):
    ID = scrapy.Field()
    Title = scrapy.Field()
    Address = scrapy.Field()
    District = scrapy.Field()
    Price = scrapy.Field()
    Price_Unit = scrapy.Field()
    Property_Type = scrapy.Field()
    Ad_Post_Date = scrapy.Field()
    Ad_Views = scrapy.Field()
    Agency = scrapy.Field()
    Seller = scrapy.Field()
    Seller_Contact = scrapy.Field()
    Seller_Email = scrapy.Field()
    Link = scrapy.Field()
