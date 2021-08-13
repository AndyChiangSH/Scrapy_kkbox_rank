# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


# class KkboxRankPipeline:
#     def process_item(self, item, spider):
#         return item


class ChinesePipeline:
    def __init__(self):
        self.file = open('chinese_rank.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class EnglishPipeline:
    def __init__(self):
        self.file = open('english_rank.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class JapanesePipeline:
    def __init__(self):
        self.file = open('japanese_rank.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class KoreanPipeline:
    def __init__(self):
        self.file = open('korean_rank.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class TaiwanesePipeline:
    def __init__(self):
        self.file = open('taiwanese_rank.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class CantonesePipeline:
    def __init__(self):
        self.file = open('cantonese_rank.csv', 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='big5')
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
