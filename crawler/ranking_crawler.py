# coding=utf-8
"""
    python 2.7
    小说排行榜
    [
        {
        "list": [
            {
                "url": "20_20623",
                "type": "科幻小说",
                "number": "1",
                "title": "幻游猎人"
            }
        ],
        "title": "小说总榜"
        },
    】

"""

import json

from bean.ranking import Ranking
from config.config import get_out_directory
from parser.html_parser import HtmlParser


class RankingCrawler(HtmlParser):
    def __init__(self, html):
        soup = HtmlParser.soup(html)

        # 获取所有板块
        blocks = soup.find_all('div', class_='block')
        blocks = self.blocks(blocks)

        self.index = blocks

    # 获取模块信息
    def blocks(self, blocks):
        result = []
        for block in blocks:
            block = self.block(block)
            result.append(block)
        return result

    # 解析单个模块
    def block(self, block):
        result = {}
        # 获取标题
        title = block.find('h2').get_text()

        rankings = []
        # 获取所有的列表
        lis = block.find_all('li')
        for li in lis:
            ranking = self.li(li)
            rankings.append(ranking)

        result['title'] = title
        result['list'] = rankings
        return result

    # 解析单个列表
    def li(self, li):
        # 排名第几
        number = li.find('em').get_text()

        a = li.find('a')
        # 标题
        title = a.get_text()
        # 小说地址
        url = a['href']

        # 小说类型
        type = li.find('span', class_='rate').get_text()

        return Ranking(number, title, url, type).to_json()

    # 获取当前解析的json
    def get_json(self):
        return json.dumps(self.index)

    # 将当前的json保存到文件中，默认为index.json
    def save_to_file(self, file_name='ranking.json'):
        open(file_name, 'w+').write(self.get_json())
        return file_name

    # 获取父类
    def get_super(self):
        return super(RankingCrawler, self)
