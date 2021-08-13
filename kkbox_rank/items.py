# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KkboxRankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_rank = scrapy.Field()
    song_name = scrapy.Field()
    song_artist = scrapy.Field()
    song_date = scrapy.Field()
    song_url = scrapy.Field()
