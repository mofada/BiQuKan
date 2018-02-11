# coding=utf-8
import re
import urlparse

from config.config import get_http


class Book(object):
    def __init__(self, title, author='', url='', cover='', description='', type=''):
        # 书籍标题
        self.__title = None
        # 书籍作者
        self.__author = None
        # 书籍地址
        self.__url = None
        # 书籍封面
        self.__cover = None
        # 书籍描述
        self.__description = None
        # 书籍类型
        self.__type = None

        # 这里进行设置，方便操作
        self.set_title(title)
        self.set_author(author)
        self.set_url(url)
        self.set_cover(cover)
        self.set_description(description)
        self.set_type(type)

    # 设置标题
    def set_title(self, title):
        self.__title = title

    # 获取标题
    def get_title(self):
        return self.__title

    # 设置作者
    def set_author(self, author):
        self.__author = author

    # 获取作者
    def get_author(self):
        return self.__author

    # 设置地址
    # 设置的url存在 /1_1094/ 去掉其中的/
    def set_url(self, url):
        if url != '':
            url = re.sub(r'/', '', url)
        self.__url = url

    # 获取地址''
    def get_url(self):
        return self.__url

    # 设置封面
    # 图片地址：/files/article/image/1/1094/1094s.jpg
    # 处理后 ： http：×××××
    # 将图片地址拼接起来
    def set_cover(self, cover):
        if cover != '':
            cover = urlparse.urljoin(get_http(), cover)
        self.__cover = cover

    # 获取封面
    def get_cover(self):
        return self.__cover

    # 设置描述
    # 需要进行处理，描述中存在空格
    def set_description(self, description):
        # 利用正则去掉空格
        self.__description = re.sub(r'\s+', '', description)

    # 获取描述
    def get_description(self):
        return self.__description

    # 设置类型
    def set_type(self, type):
        self.__type = type

    # 获取类型
    def get_type(self):
        return self.__type

    # 将实体类转化为json
    def to_json(self):
        return {
            'title': self.__title,
            'author': self.__author,
            'url': self.__url,
            'cover': self.__cover,
            'description': self.__description,
            'type': self.__type,
        }
