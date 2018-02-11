# coding=utf-8
"""
    python 2.7
    首页
"""
import json

import os

import config
from config.config import get_http, get_index_book_type, save_chapter_info, file_exist, get_chapter_info_by_file
from crawler.book_info_crawler import BookInfoCrawler
from crawler.chapter_info_crawler import ChapterInfoCrawler
from crawler.index_crawler import IndexCrawler
from crawler.index_type_crawler import IndexTypeCrawler
from crawler.query_crawler import QueryCrawler
from crawler.ranking_crawler import RankingCrawler
from html_download.html_download import HtmlDownload


class BiQuKan(object):
    # 获取首页json
    def get_index(self):
        html = HtmlDownload.download(get_http())
        return IndexCrawler(html)

    # 根据小说id获取书籍信息
    def get_book_info(self, book_url):
        if book_url is None:
            return
        url = get_http() + book_url
        html = HtmlDownload.download(url)
        return BookInfoCrawler(html)

    # 获取章节信息
    def get_chapter_info(self, book_url, chapter_url):
        if book_url is None or chapter_url is None:
            return
        url = get_http() + '%s/%s.html' % (book_url, chapter_url)
        html = HtmlDownload.download(url)
        chapter_info = ChapterInfoCrawler(html)
        save_chapter_info(book_url, chapter_url, chapter_info.get_json())
        return chapter_info

    # 小说类型
    # 0 玄幻小说
    # 1 修真小说
    # 2 都市小说
    # 3 穿越小说
    # 4 网游小说
    # 5 科幻小说
    # 6 其他小说
    # 7 完本小说
    def get_index_type(self, type=0):
        type = get_index_book_type(type)
        html = HtmlDownload.download(get_http() + type)
        return IndexTypeCrawler(html)

    # 查询
    def get_query(self, query, page=0):
        if query is None or query == '':
            return
        # query = quote(query)
        url = 'http://zhannei.baidu.com/cse/search?p=%s&q=%s&s=2758772450457967865&srt=def&nsid=0&click=1' % (page, query)
        html = HtmlDownload.download(url)
        return QueryCrawler(html)

    # 获取小说排行榜
    def get_ranking(self):
        html = HtmlDownload.download(get_http() + 'paihangbang')
        return RankingCrawler(html)

    # 下载单个章节
    def download_chapter(self, book_url, chapter_url):
        chapter = ''
        if file_exist(book_url, chapter_url):
            chapter = get_chapter_info_by_file(book_url, chapter_url)
        else:
            chapter = self.get_chapter_info(book_url, chapter_url).get_json()
        return chapter

    # 下载小说
    def download_chapters(self, book_url):
        result = ''
        chapters = self.get_book_info(book_url).get_book_chapters()
        count = len(chapters)
        current = 0
        for chapter in chapters:
            try:
                print '%d/%d' % (current, count)
                chapter_url = chapter['url']
                chapter = self.download_chapter(book_url, chapter_url)
                result += chapter + ','
            except Exception, e:
                continue
            current += 1
        return '[' + result[:-1] + ']'
