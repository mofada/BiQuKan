# coding=utf-8
"""
    python 2.7
    首页解析——地址：http://www.biqukan.com/
    结果解析——json
    {
        items： --最上面的4个推荐
        [
            {
                "description": "吾有一口玄黄气，可吞天地日月星。", --小说描述
                "author": "天蚕土豆", --小说作者
                "url": "0_790", --小说id
                "title": "元尊", --小说标题
                "cover": "http://www.biqukan.com/files/article/image/0/790/790s.jpg", --小说封面
                "type": "" --小说类型
            }
        ]
        hot_lis： --强力推荐
        [
            {--同item
                "description": "",
                "author": "耳根",
                "url": "0_784",
                "title": "滇娇传之天悦东方",
                "cover": "",
                "type": "修真"
            }
        ]
        blocks： --中间六个模块，玄幻小说之类的
        [
            --封面图
            "top": { --同item
                "description": "......",
                "author": "",
                "url": "20_20951",
                "title": "独步天途",
                "cover": "http://www.biqukan.com/images/nocover.jpg",
                "type": ""
            },
            "lis":[
                { --同item
                    "description": "",
                    "author": "鹅城知县",
                    "url": "30_30398",
                    "title": "青云直上",
                    "cover": "",
                    "type": ""
                },
            ],
            "title": "玄幻小说" --标题
        ]
        update：最近更新小说列表
        [
            "title": " 最近更新小说列表" --标题
            lis:[
                {
                    "update_time": "02-05", --更新时间
                    "author": "二十二刀流", --作者
                    "url": "25_25778", --小说id
                    "title": "末世大回炉", --小说标题
                    "update_url": "17921507", --更新地址
                    "type": "科幻小说", --小说类型
                    "update_chapter": "第1848章 进城" --更新章节
                },
            ]
        ]
        storage：最新入库小说 --同最近更新小说列表
    }
"""
import json

from bean.book import Book
from config.config import get_out_directory
from parser.html_parser import HtmlParser


class IndexCrawler(HtmlParser):
    def __init__(self, html):
        index = {}

        soup = HtmlParser.soup(html)

        # hot 部分
        items, hot_lis = self.hot(soup)

        # block
        blocks = self.type_bd(soup)

        # up
        update, storage = self.up(soup)

        index['items'] = items
        index['hot_lis'] = hot_lis
        index['blocks'] = blocks
        index['update'] = update
        index['storage'] = storage

        self.index = index

    def up(self, soup):
        # 获取up
        up = soup.find('div', class_='up')

        # 最近更新小说列表
        update = up.find('div', class_='l bd')
        update = self.update(update)

        # 最新入库小说
        storage = up.find('div', class_='r bd')
        storage = self.storage(storage)

        return update, storage

    # 最近更新小说列表
    def storage(self, storage):
        return self.get_super().update(storage)

    # 最近更新小说列表
    def update(self, update):
        return self.get_super().update(update)

    # 获取 type bd
    def type_bd(self, soup):
        # 获取所有的block
        blocks = soup.find_all('div', class_='block')
        blocks = self.blocks(blocks)
        return blocks

    # 解析block
    def blocks(self, blocks):
        result = []

        for block in blocks:
            block_item = {}
            # 获取标题
            h2 = block.find('h2').get_text()

            # 获取top
            top = block.find('div', class_='top')

            cover = top.find('div', class_='image').find('img')['src']

            # 获取超链接
            a = top.find('dt').find('a')

            # 获取链接
            url = a['href']

            # 获取标题
            title = a.get_text()

            # 获取描述
            description = top.find('dd').get_text()

            lis = block.find_all('li')

            book = Book(title, '', url, cover, description)

            # 解析所有的lis
            block_lis = self.block_lis(lis)

            block_item['title'] = h2
            block_item['top'] = book.to_json()
            block_item['lis'] = block_lis
            result.append(block_item)
        return result

    def block_lis(self, lis):
        result = []

        for li in lis:
            '''
            <li>
                <a href="/30_30398/" target="_blank" title="青云直上">青云直上</a>/鹅城知县
            </li>
            '''
            a = li.find('a')

            # 地址
            url = a['href']

            text = li.get_text().split(u'/')
            # 标题
            title = text[0]

            # 作者
            author = text[-1]

            book = Book(title, author, url)
            result.append(book.to_json())
        return result

    def hot(self, soup):
        # 获取所有的items
        items = soup.find_all('div', class_='item')
        items = self.hot_items(items)

        # 获取强力推荐
        ul = soup.find('ul', class_='lis')
        # 获取所有的lis
        lis = ul.find_all('li')
        hot_lis = self.hot_lis(lis)

        return items, hot_lis

    # 获取所有的li
    def hot_lis(self, lis):
        result = []
        for li in lis:
            '''
            <li>
                 <span class="s1">[修真]</span>
                 <span class="s2">
                       <a href="/0_784/">滇娇传之天悦东方</a>
                 </span><span class="s5">耳根</span>
            </li>
            '''
            # book = {}

            # 获取书籍的类型
            type = li.find('span', class_='s1').get_text()
            # 替换类型的 []
            type = self.get_super().re_type(type)

            s2_a = li.find('span', class_='s2').find('a')
            # 获取书籍地址
            url = s2_a['href']
            # 获取书籍标题
            title = s2_a.get_text()

            author = li.find('span', class_='s5').get_text()

            book = Book(title, author, url, type=type)
            result.append(book.to_json())
        return result

    # 获取items
    def hot_items(self, items):
        return self.get_super().hot_items(items)

    # 获取当前解析的json
    def get_json(self):
        return json.dumps(self.index)

    # 将当前的json保存到文件中，默认为index.json
    def save_to_file(self, file_name='index.json'):
        open(file_name, 'w+').write(self.get_json())
        return file_name

    # 获取父类
    def get_super(self):
        return super(IndexCrawler, self)
