# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TiebaspiderPipeline(object):

    def __init__(self):
        self.file = open(
            '/home/fy/workspaces/spider/test_scrapy/mySpider/mySpider/title.txt', 'wb')

    def process_item(self, item, spider):
        self.file.write(item['title'] + '\n')
        return item

    def close_spider(self, spider):
        self.file.close()