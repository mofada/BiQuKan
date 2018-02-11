# coding=utf-8
"""
    python 2.7
    返回结果同index
"""

import json

from config.config import get_out_directory
from parser.html_parser import HtmlParser


class IndexTypeCrawler(HtmlParser):
    def __init__(self, html):
        index = {}

        soup = HtmlParser.soup(html)

        # 获取热门
        hot = soup.find('div', class_='hot')
        # 获取所有的item
        items = self.hot_items(hot)

        # 最近更新小说列表,最新入库小说
        update, storage = self.up(soup)

        index['items'] = items
        index['update'] = update
        index['storage'] = storage

        self.index = index

    def up(self, soup):
        # 获取up
        up = soup.find('div', class_='up')

        # 最近更新小说列表
        update = up.find('div', class_='l bd')
        update = self.update(update)

        # 最新入库小说
        storage = up.find('div', class_='r bd')
        storage = self.storage(storage)

        return update, storage

    # 最近更新小说列表
    def storage(self, storage):
        return self.get_super().update(storage)

    # 最近更新小说列表
    def update(self, update):
        return self.get_super().update(update)

    def hot_items(self, hot):
        items = hot.find_all('div', class_='item')
        return self.get_super().hot_items(items)

    # 获取当前解析的json
    def get_json(self):
        return json.dumps(self.index)

    # 将当前的json保存到文件中，默认为index.json
    def save_to_file(self, file_name='index_type.json'):
        open(file_name, 'w+').write(self.get_json())
        return file_name

    # 获取父类
    def get_super(self):
        return super(IndexTypeCrawler, self)
