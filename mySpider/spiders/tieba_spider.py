# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import TiebaspiderItem
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class TiebaSpiderSpider(scrapy.Spider):
    name = 'tieba_spider'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=一击男&ie=utf-8&pn=0']

    def parse(self, response):
        # items = []
        soup = BeautifulSoup(response.body, 'lxml')
        # print soup
        titles = soup.select('div.threadlist_lz.clearfix > div > a')
        for title in titles:
            item = TiebaspiderItem()
            item['title'] = title.get('title')
            # items.append(item)

            yield item
            # 证明位置无影响，这取决于获取url的机制
            curpage = re.search(r'pn=(\d+)', response.url).group(1)
            if int(curpage) < (50*6):
                curpage = int(curpage) + 50
            url = re.sub(r'=(\d+)', '=' + str(curpage), response.url)
            yield scrapy.Request(url, callback=self.parse)
        # curpage = re.search(r'pn=(\d+)', response.url).group(1)
        # if int(curpage) < (50*6):
        #     curpage = int(curpage) + 50
        # url = re.sub(r'=(\d+)', '=' + str(curpage), response.url)
        # yield scrapy.Request(url, callback=self.parse)

        # return items
