# coding=utf-8
import os

from biqukan.biqukan import BiQuKan

if __name__ == '__main__':
    # 实例化biqukan对象
    biqukan = BiQuKan()
    # 获取首页数据 http://www.biqukan.com/
    biqukan.get_index().get_json()

    # 根据小说id获取小说信息 http://www.biqukan.com/1_1094
    biqukan.get_book_info('1_1094').get_json()

    # 根据小说id和章节id获取章节信息 http://www.biqukan.com/1_1094/17967679.html
    biqukan.get_chapter_info('1_1094', '17967679')

    # 获取首页类型小说 http://www.biqukan.com/xuanhuanxiaoshuo/
    # 0 玄幻小说 默认是玄幻小说
    # 1 修真小说
    # 2 都市小说
    # 3 穿越小说
    # 4 网游小说
    # 5 科幻小说
    # 6 其他小说
    # 7 完本小说
    biqukan.get_index_type().get_json()

    # 查询小说
    # http://zhannei.baidu.com/cse/search?q=%E4%BA%94%E8%A1%8C%E5%A4%A9&click=1&s=2758772450457967865&nsid=
    biqukan.get_query('五行天', page=0).save_to_file()

    # 小说排行榜 http://www.biqukan.com/paihangbang/
    biqukan.get_ranking().save_to_file()

    # 下载单个章节 http://www.biqukan.com/1_1094/17967679.html
    biqukan.download_chapter('1_1094', '17967679')

    # 下载整个书籍的章节
    biqukan.download_chapters('1_1094')
