# coding=utf-8
import re
import urlparse

from bean.book_info import BookInfo
from config.config import get_http


class BookQuery(object):
    def __init__(self, cover='', title='', url='', author='', type='', status='', word_count='', update_time='',
                 update_chapter='', update_url='', description=''):

        # 书籍封面
        self.__cover = None
        # 书籍地址
        self.__url = None
        # 书籍标题
        self.__title = None
        # 书籍作者
        self.__author = None
        # 书籍类型
        self.__type = None
        # 书籍状态
        self.__status = None
        # 书籍字数
        self.__word_count = None
        # 书籍更新时间
        self.__update_time = None
        # 书籍最新章节
        self.__update_chapter = None
        # 书籍最新章节地址
        self.__update_url = None
        # 书籍描述
        self.__description = None

        # 设置属性
        self.set_cover(cover)
        self.set_title(title)
        self.set_url(url)
        self.set_author(author)
        self.set_type(type)
        self.set_status(status)
        self.set_word_count(word_count)
        self.set_update_time(update_time)
        self.set_update_chapter(update_chapter)
        self.set_update_url(update_url)
        self.set_description(description)

    # 设置小说地址
    def set_url(self, url):
        if url != '':
            url = re.match(r'(.*)/(\d+_\d+)/', url).group(2)
        self.__url = url

    # 获取小说地址
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

    # 设置标题
    def set_title(self, title):
        title = re.sub(r'\s+', '', title)
        self.__title = title

    # 获取标题
    def get_title(self):
        return self.__title

    # 设置作者
    def set_author(self, author):
        author = re.sub(r'\s+', '', author)
        self.__author = author

    # 获取作者
    def get_author(self):
        return self.__author

    # 设置类型
    def set_type(self, type):
        type = re.sub(r'\s+', '', type)
        self.__type = type

    # 获取类型
    def get_type(self):
        return self.__type

    # 设置状态
    def set_status(self, status):
        self.__status = status

    # 获取状态
    def get_status(self):
        return self.__status

    # 设置总字数
    def set_word_count(self, word_count):
        self.__word_count = word_count

    # 获取总字数
    def get_word_count(self):
        return self.__word_count

    # 设置更新时间
    def set_update_time(self, update_time):
        update_time = re.sub(r'\s+', '', update_time)
        self.__update_time = update_time

    # 获取更新时间
    def get_update_time(self):
        return self.__update_time

    # 设置更新章节
    def set_update_chapter(self, update_chapter):
        update_chapter = re.sub(r'\s+', '', update_chapter)
        self.__update_chapter = update_chapter

    # 获取更新章节
    def get_update_chapter(self):
        return self.__update_chapter

    # 设置更新章节地址
    # 书籍地址 (/1_1094/17918892.html)
    # 修改后 17918892
    def set_update_url(self, update_url):
        if update_url != '':
            update_url = re.match(r'(.*)/(\d+).html', update_url).group(2)
        self.__update_url = update_url

    # 获取更新章节地址
    def get_update_url(self):
        return self.__update_url

    # 设置书籍描述
    # 描述 ： ×××××作者
    # 包含作者两个字，去掉
    def set_description(self, description):
        description = re.sub(r'\s+', '', description)
        self.__description = description

    # 获取书籍描述
    def get_description(self):
        return self.__description

    # 将实体类转化为json
    def to_json(self):
        return {
            'cover': self.__cover,
            'url': self.__url,
            'title': self.__title,
            'author': self.__author,
            'type': self.__type,
            'status': self.__status,
            'word_count': self.__word_count,
            'update_time': self.__update_time,
            'update_chapter': self.__update_chapter,
            'update_url': self.__update_url,
            'description': self.__description,
        }
