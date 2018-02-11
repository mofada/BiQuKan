# coding=utf-8
import re
import urlparse

from bean.book import Book
from config.config import get_http


class BookLi(object):
    def __init__(self, type, title, url, update_time, update_chapter='', author='', update_url=''):
        # 小说类型
        self.__type = None
        # 小说标题
        self.__title = None
        # 小说地址
        self.__url = None
        # 小说更新时间
        self.__update_time = None
        # 小说更新章节
        self.__update_chapter = None
        # 小说作者
        self.__author = None
        # 小说更新章节地址
        self.__update_url = None

        self.set_type(type)
        self.set_title(title)
        self.set_url(url)
        self.set_update_time(update_time)
        self.set_update_chapter(update_chapter)
        self.set_author(author)
        self.set_update_url(update_url)

    # 设置类型
    def set_type(self, type):
        self.__type = type

    # 获取类型
    def get_type(self):
        return self.__type

    # 设置标题
    def set_title(self, title):
        self.__title = title

    # 获取标题
    def get_title(self):
        return self.__title

    # 设置地址
    # 设置的url存在 /1_1094/ 去掉其中的/
    def set_url(self, url):
        self.__url = re.sub(r'/', '', url)

    # 获取地址''
    def get_url(self):
        return self.__url

    # 设置更新时间
    def set_update_time(self, update_time):
        self.__update_time = update_time

    # 获取更新时间
    def get_update_time(self):
        return self.__update_time

    # 设置更新章节
    def set_update_chapter(self, update_chapter):
        self.__update_chapter = update_chapter

    # 获取更新章节
    def get_update_chapter(self):
        return self.__update_chapter

    # 设置作者
    def set_author(self, author):
        self.__author = author

    # 获取作者
    def get_author(self):
        return self.__author

    # 设置更新章节地址
    # 书籍地址 (/1_1094/17918892.html)
    # 修改后 17918892
    def set_update_url(self, update_url):

        if update_url != '':
            update_url = re.match(r'/(\d+)_(\d+)/(\d+).html', update_url).group(3)
        self.__update_url = update_url

    # 获取更新章节地址
    def get_update_url(self):
        return self.__update_url

    # 将实体类转化为json
    def to_json(self):
        return {
            'type': self.__type,
            'title': self.__title,
            'url': self.__url,
            'update_time': self.__update_time,
            'update_chapter': self.__update_chapter,
            'author': self.__author,
            'update_url': self.__update_url,
        }
