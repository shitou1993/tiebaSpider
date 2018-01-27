#!/home/fy/.virtualenvs/spider_py2/bin/python2.7
# coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys


def loadpages(url, start_page, end_page):
    for page in range(int(start_page), int(end_page) + 1):
        pn = (page - 1) * 50
        url = url + '&ie=utf-8&pn=' + str(pn)
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
            'Connection': 'keep-alive',
        }

        print(page)
        file_name = '/home/fy/文档/spider/tieba/' + '第' + str(page) + '页'
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
        # print html
        sparse(html, file_name)


def sparse(html, file_name):
    text = BeautifulSoup(html, 'lxml')
    # print text
    titles = text.select(
        'div.threadlist_lz.clearfix > div > a')
    # print titles
    write_file(file_name, titles)


def write_file(file_name, titles):
    with open(file_name, 'w')as f:
        for title in titles:
            print title.get('title')
            f.write(title.get('title') + '\n')


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')	
    tieba_name = raw_input('请输入希望抓取的贴吧名称')
    keyword = {'kw': tieba_name}
    keyword = urllib.urlencode(keyword)
    url = 'https://tieba.baidu.com/f?' + keyword
    start_page = raw_input('请输入起始页码')
    end_page = raw_input('请输入截止页码')
    loadpages(url, start_page, end_page)
