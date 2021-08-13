import scrapy
import requests
import json
import time


class ChineseRankSpider(scrapy.Spider):
    name = 'chinese_rank'
    allowed_domains = ['kma.kkbox.com', 'www.kkbox.com']
    start_urls = [
        'https://kma.kkbox.com/charts/api/v1/daily?category=297&lang=tc&limit=50&terr=tw&type=newrelease']

    def parse(self, response):
        # print(response.text)
        data = json.loads(response.text)
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
            yield KkboxRankItem
