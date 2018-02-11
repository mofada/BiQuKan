# coding=utf-8
import re


class Ranking(object):
    def __init__(self, number, title, url, type):
        # 小说排行榜排名
        self.__number = None
        # 书籍标题
        self.__title = None
        # 书籍地址
        self.__url = None
        # 书籍类型
        self.__type = None

        # 这里进行设置，方便操作
        self.set_number(number)
        self.set_title(title)
        self.set_url(url)
        self.set_type(type)

    # 设置作者
    def set_number(self, number):
        self.__number = number

    # 获取作者
    def get_number(self):
        return self.__number

    # 设置标题
    def set_title(self, title):
        self.__title = title

    # 获取标题
    def get_title(self):
        return self.__title

    # 设置地址
    # 设置的url存在 /1_1094/ 去掉其中的/
    def set_url(self, url):
        if url != '':
            url = re.sub(r'/', '', url)
        self.__url = url

    # 获取地址''
    def get_url(self):
        return self.__url

    # 设置类型
    def set_type(self, type):
        self.__type = type

    # 获取类型
    def get_type(self):
        return self.__type

    # 将实体类转化为json
    def to_json(self):
        return {
            'number': self.__number,
            'title': self.__title,
            'url': self.__url,
            'type': self.__type,
        }
