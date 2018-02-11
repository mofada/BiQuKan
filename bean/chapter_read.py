# coding=utf-8
import re


class ChapterRead(object):
    def __init__(self, title, text_list, text, previous, list, next):
        # 标题
        self.__title = None
        # 内容列表
        self.__text_list = None
        # 内容文字
        self.__text = None
        # 上一章节
        self.__previous = None
        # 章节目录
        self.__list = None
        # 下一章节
        self.__next = None

        self.set_title(title)
        self.set_text_list(text_list)
        self.set_text(text)
        self.set_previous(previous)
        self.set_list(list)
        self.set_next(next)

    # 设置标题
    def set_title(self, title):
        self.__title = title

    # 获取标题
    def get_title(self):
        return self.__title

    # 设置内容列表
    def set_text_list(self, text_list):
        self.__text_list = text_list

    # 获取内容列表
    def get_text_list(self):
        return self.__text_list

    # 设置内容文字
    def set_text(self, text):
        self.__text = text

    # 获取内容文字
    def get_text(self):
        return self.__text

    # 设置上一章节
    def set_previous(self, previous):
        self.__previous = self.get_chapter_url(previous)

    # 获取上一章节
    def get_previous(self):
        return self.__previous

    # 设置章节目录
    def set_list(self, list):
        if list != '':
            list = re.sub(r'/', '', list)
        self.__list = list

    # 获取章节目录
    def get_list(self):
        return self.__list

    # 设置下一章节
    def set_next(self, next):
        self.__next = self.get_chapter_url(next)

    # 获取下一章节
    def get_next(self):
        return self.__next

    # 将实体类转化为json
    def to_json(self):
        return {
            'title': self.__title,
            'text_list': self.__text_list,
            'text': self.__text,
            'previous': self.__previous,
            'list': self.__list,
            'next': self.__next,
        }

    def get_chapter_url(self, chapter_url):
        match = re.match(r'/(\d+)_(\d+)/(\d+).html', chapter_url)
        if match:
            return match.group(3)
        else:
            return ''
