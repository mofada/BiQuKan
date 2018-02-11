# coding=utf-8

"""
    python 2.7
    小说阅读解析
    {
        "title": "第1305章 逆陨", --章节标题
        "text_list": [  --章节内容list
            "　　第二指，无声无息点出的瞬间，白小纯的头发直接就花白了一半，他的皮肤也似乎失去了光泽，他的生命，他的生机在这一刹那消失，化作了无形之力，去与星空大道共鸣，去与那永恒本源形成的玄妙共鸣！",
            "　　就算是这样，它那看似无尽的生机，也都被吸走了只剩一丝，才可以让白小纯，加上自己的余力，展开第四指！",
            "　　此刻在这第四指下，星空波澜不起，白小纯疲惫中，眼睛慢慢闭上，似没有睁开的力气，他的身体也失去了支撑，向着永恒仙域的方向，慢慢的飘落……在他双眼闭合的瞬间，灭圣发出前所未有的嘶吼。"
        ],
        "list": "1_1094", --章节目录
        "next": “17927946", --下一章节
        "text": "　　第二指，，入的黑芒，使得其身体外这一瞬，的飘落……在他双眼闭合的瞬间，灭圣发出前所未有的嘶吼。", --章节内容文字
        "previous": "17916686" --上一章节
    }

"""

import json

from bs4 import NavigableString

from bean.chapter_read import ChapterRead
from parser.html_parser import HtmlParser


class ChapterInfoCrawler(HtmlParser):
    def __init__(self, html):
        soup = HtmlParser.soup(html)

        # 获取内容
        content = soup.find('div', class_='content')

        # 首先获取标题
        title = content.find('h1').get_text()

        # 获取文字内容
        showtxt = content.find('div', class_='showtxt')
        # 对内容进行处理
        text_list = self.showtxt(showtxt)
        text = '\n'.join(text_list)

        # 获取page_chapter
        page_chapter = content.find('div', class_='page_chapter')

        # 获取导航
        nav = page_chapter.find_all('a')

        # 获取上一章节
        previous = nav[0]['href']

        # 目录
        list = nav[1]['href']

        # 下一章节
        next = nav[2]['href']

        self.chapter_read = ChapterRead(title, text_list, text, previous, list, next)

    # 对文字进行处理
    def showtxt(self, showtxt):
        contents = showtxt.contents
        text = []
        for content in contents:
            # 内容是否是NavigableString的实例，true-是文字，false是标签，舍弃
            if isinstance(content, NavigableString):
                # 将字符转化为utf-8编码，并替换其中的空格
                string = content.string.encode('utf-8').replace(' ', '')
                text.append(string)
        return text[:-2]

    def get_json(self):
        return json.dumps(self.chapter_read.to_json())

    def save_to_file(self, file_name='chapter_read.json'):
        open(file_name, 'w+').write(self.get_json())
        return file_name
