# coding=utf-8

# 获取http
import os


def get_http():
    return 'http://www.biqukan.com/'


# 获取输出目录
def get_out_directory():
    return '/out/'


books_types = (
    'xuanhuanxiaoshuo', 'xiuzhenxiaoshuo', 'dushixiaoshuo', 'chuanyuexiaoshuo', 'wangyouxiaoshuo', 'kehuanxiaoshuo',
    'qitaxiaoshuo', 'wanben')


# 0 玄幻小说
# 1 修真小说
# 2 都市小说
# 3 穿越小说
# 4 网游小说
# 5 科幻小说
# 6 其他小说
# 7 完本小说
def get_index_book_type(type=0):
    if type < 0 or type >= len(books_types):
        type = 0
    return books_types[type]


# 存储章节信息
def save_chapter_info(book_url, chapter_url, chapter_info):
    file = open(get_file_name(book_url, chapter_url), 'w+')
    file.write(chapter_info)


# 获取章节信息
def get_chapter_info_by_file(book_url, chapter_url):
    file = open(get_file_name(book_url, chapter_url), 'r')
    return file.read()


# 判断章节文件是否存在
def file_exist(book_url, chapter_url):
    return os.path.exists(get_file_name(book_url, chapter_url))


def get_file_name(book_url, chapter_url):
    return 'chapters/%s-%s' % (book_url, chapter_url)
