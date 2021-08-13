# 爬取最新西洋歌曲前50名

import scrapy
import requests
import json
import time


class EnglishRankSpider(scrapy.Spider):
    name = 'english_rank'
    allowed_domains = ['kma.kkbox.com']
    start_urls = [
        'https://kma.kkbox.com/charts/api/v1/daily?category=390&lang=tc&limit=50&terr=tw&type=newrelease']
    custom_settings = {
        'ITEM_PIPELINES': {
            'kkbox_rank.pipelines.EnglishPipeline': 400
        }
    }

    def parse(self, response):
        # print(response.text)
        data = json.loads(response.text)    # from json to dict
        song_list = data["data"]["charts"]["newrelease"]
        for song in song_list:
            song_rank = song["rankings"]["this_period"]
            song_name = song["song_name"]
            song_url = song["song_url"]
            song_artist = song["artist_name"]
            song_timestamp = int(song["release_date"])
            song_date = time.strftime(
                "%Y-%m-%d", time.localtime(song_timestamp))  # from timestamp to time string

            KkboxRankItem = {
                "song_rank": song_rank,
                "song_name": song_name,
                "song_artist": song_artist,
                "song_date": song_date,
                "song_url": song_url,
            }

            yield KkboxRankItem  # return item
