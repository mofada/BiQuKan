# coding=utf-8
import json

from bean.book_query import BookQuery
from config.config import get_out_directory
from parser.html_parser import HtmlParser


class QueryCrawler(HtmlParser):
    def __init__(self, html):
        soup = HtmlParser.soup(html)

        # 获取数据列表，只关心数据，其他的不管
        result_list = soup.find('div', class_='result-list')

        # 获取result-item，数据列表
        result_items = result_list.find_all('div', class_='result-item')
        result_items = self.result_items(result_items)

        self.index = result_items

    def result_items(self, items):
        result = []
        for item in items:
            book = self.item(item)
            result.append(book)
        return result

    # 解析item
    def item(self, item):
        # 获取封面图片
        pic = item.find('div', class_='result-game-item-pic')

        # 获取封面
        cover = pic.find('img')['src']

        detail = item.find('div', class_='result-game-item-detail')

        a = detail.find('a')
        # 标题
        title = a.get_text()

        # 获取地址
        url = a['href']

        # 获取描述
        description = item.find('p', class_='result-game-item-desc').get_text()

        info = item.find('div', class_='result-game-item-info')
        info_p_ = info.find_all('p')

        # 小说作者
        author = self.info_p(info_p_[0])

        # 小说类型
        type = self.info_p(info_p_[1])

        # 小说更新时间
        update_time = self.info_p(info_p_[2])

        # 小说最新章节
        update_chapter = self.info_p(info_p_[3])

        # 小说最新章节地址
        update_url = info.find('a')['href']

        book_info = BookQuery(cover=cover, title=title, url=url, author=author, type=type, update_time=update_time,
                              update_chapter=update_chapter, update_url=update_url, description=description)
        return book_info.to_json()

    def info_p(self, span):
        text = span.get_text()
        split = text.split(u'：')
        return split[-1]

    def get_json(self):
        return json.dumps(self.index)

    def save_to_file(self, file_name='query.json'):
        open(file_name, 'w+').write(self.get_json())
        return file_name
