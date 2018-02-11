# coding=utf-8
import re
from bs4 import BeautifulSoup

from bean.book import Book
from bean.book_li import BookLi


class HtmlParser(object):
    @staticmethod
    def soup(html):
        return BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

    # 首页中的最近更新小说
    def update(self, update):
        result = {}
        # 获取标题
        title = update.find('h2').get_text()
        # 获取列表
        lis = update.find_all('li')
        lis = self.update_lis(lis)

        result['title'] = title
        result['lis'] = lis
        return result

    # 解析index storage下的lis
    def storage(self, storage):
        return self.update(storage)

    # 解析index update下的lis
    def update_lis(self, lis):
        result = []
        for li in lis:
            # 获取书籍类型
            type = li.find('span', class_='s1').get_text()
            type = self.re_type(type)

            # 获取超链接
            s2_a = li.find('span', class_='s2').find('a')
            # 标题
            title = s2_a.get_text()
            # 地址
            url = s2_a['href']

            # 更新章节
            update_chapter = ''
            # 更新地址
            update_url = ''
            s3 = li.find('span', class_='s3')
            if s3 is not None:
                s3_a = s3.find('a')
                # 更新章节
                update_chapter = s3_a.get_text()
                # 更新地址
                update_url = s3_a['href']

            # 获取作者
            s4 = li.find('span', class_='s4')
            author = ''
            if s3 is not None:
                author = li.find('span', class_='s4').get_text()

            # 获取时间
            update_time = li.find('span', class_='s5').get_text()

            book = BookLi(type, title, url, update_time, update_chapter, author, update_url)
            result.append(book.to_json())
        return result

    # 获取index hot items
    def hot_items(self, items):

        result = []

        for item in items:
            # book = {}
            '''
            <div class="image">
                    <a href="/0_790/" target="_blank">
                        <img src="/files/article/image/0/790/790s.jpg" alt="元尊">
                    </a>
                </div>
            '''
            # 获取最外层的div
            class_image = item.find('div', class_='image')
            # 书籍地址
            url = class_image.find('a')['href']
            # 书籍封面
            cover = class_image.find('img')['src']

            '''
            <dl>
                <dt>
                    <span>天蚕土豆</span>
                    <a href="/0_790/" target="_blank">元尊</a>
                </dt>
                <dd> 吾有一口玄黄气，可吞天地日月星。</p>
                            ......
                </dd>
            </dl>
            '''
            # 获取最外层的dl
            dl = item.find('dl')

            # 获取次一层的dt
            dt = dl.find('dt')
            # 获取作者名
            author = dt.find('span').get_text()
            # 获取书名
            title = dt.find('a').get_text()

            # 获取书籍描述
            description = dl.find('dd').get_text()

            book = Book(title, author, url, cover, description)
            result.append(book.to_json())

        return result

    def re_type(self, type):
        return re.sub(r'\[|\]', '', type)

    # 获取json数据
    def get_json(self):
        pass

    # 以文件形式保存
    def save_to_file(self, file_name='query.json'):
        pass
