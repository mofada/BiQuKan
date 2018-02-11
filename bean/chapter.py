# coding=utf-8
import re


class Chapter(object):
    def __init__(self, title, url):
        # 章节标题
        self.__title = None
        # 章节地址
        self.__url = None

        # 进行设置
        self.set_title(title)
        self.set_url(url)

    # 设置地址
    # 书籍地址 (/1_1094/17918892.html)
    # 修改后 17918892
    def set_url(self, url):
        if url != '':
            url = re.match(r'/(\d+)_(\d+)/(\d+).html', url).group(3)
        self.__url = url

    # 获取地址''
    def get_url(self):
        return self.__url

    # 设置标题
    def set_title(self, title):
        if title != '':
            title = title.replace('biqukan.com', '')
        self.__title = title

    # 获取标题
    def get_title(self):
        return self.__title

    def __hash__(self):
        return self.__url

    def to_json(self):
        return {
            'title': self.__title,
            'url': self.__url,
        }
