# coding=utf-8
"""
    python 2.7 小说详情界面
    json介绍
    {
        "status": "连载", --小说状态
        "update_time": "2018-02-06 17:50:00", -- 更新时间
        "description": "一念成沧海，一念化桑田。一念斩千魔，一念诛万仙。唯我念……永恒", --小说描述、简介
        "chapters": [ --所有章节
            {
                "url": "5386269", --章节id、章节地址
                "title": "外传1 柯父。" --章节标题
            }
        ],
        "word_count": "3672172", --小说字数
        "title": "一念永恒", --小说标题
        "author": "耳根", --小说作者
        "cover": "http://www.biqukan.com/files/article/image/1/1094/1094s.jpg", --小说封面
        "update_url": "17930894", --最新章节地址
        "type": "玄幻小说", --小说类型
        "update_chapter": "第1307章 起源" --小说最新章节标题
    }

"""

import json
from bean.book_info import BookInfo
from bean.chapter import Chapter
from parser.html_parser import HtmlParser


class BookInfoCrawler(HtmlParser):
    def __init__(self, html):
        self.index = {}
        if html is not None:
            self.crawler(html)


    def crawler(self, html):
        soup = HtmlParser.soup(html)
        # 获取info
        info = soup.find('div', class_='info')
        self.index = self.info(info)

        # 获取 listmain
        listmain = soup.find('div', class_='listmain')
        # 正文章节
        chapters = listmain.find_all('a')
        chapters = self.chapters(chapters)
        self.index['chapters'] = chapters

    # 获取章节
    def chapters(self, chapters):
        # 处理章节，前12条为最近更新章节
        chapters = self.deal_with_chapters(chapters)

        result = []
        for chapter in chapters:
            # 获取章节信息
            book = self.chapter(chapter)
            # 如果章节已经不在list里，就添加
            if not self.chapter_in_list(book, result):
                result.append(book)

        return result

    def deal_with_chapters(self, chapters):
        length = len(chapters)
        if length > 24:
            chapters = chapters[12:]
        elif length > 12:
            chapters = chapters[length / 2:]
        return chapters

    # 解析章节
    def chapter(self, chapter):
        # 章节标题
        title = chapter.get_text()
        # 章节地址
        url = chapter['href']
        return Chapter(title, url).to_json()

    # 解析书籍信息
    def info(self, info):
        # 获取封面
        cover = info.find('div', class_='cover').find('img')['src']

        # 获取标题
        title = info.find('h2').get_text()

        small = info.find('div', class_='small')
        # 作者、类型、状态、字数、更新时间、最新章节
        spans = small.find_all('span')

        # 作者
        author = self.span(spans[0])

        # 类型
        type = self.span(spans[1])

        # 状态
        status = self.span(spans[2])

        # 字数
        word_count = self.span(spans[3])

        # 更新时间
        update_time = self.span(spans[4])

        # 最新章节
        update_chapter = self.span(spans[5])

        # 最新章节地址
        update_url = spans[5].find('a')['href']

        # 获取描述
        description = info.find('div', class_='intro').get_text().split(u'：')[1]

        book_info = BookInfo(cover, title, author, type, status, word_count, update_time, update_chapter, update_url,
                             description)
        return book_info.to_json()

    def span(self, span):
        text = span.get_text()
        split = text.split(u'：')
        return split[-1]

    # 获取所有的章节
    def get_book_chapters(self):
        return self.index['chapters']

    def get_json(self):
        return json.dumps(self.index)

    def save_to_file(self, file_name='book_info.json'):
        open(file_name, 'w+').write(self.get_json())
        return file_name

    def chapter_in_list(self, chapter_, chapters):
        for chapter in chapters:
            if chapter_['url'] == chapter['url']:
                return True
        return False
