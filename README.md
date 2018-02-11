# BiQuKan
基于python2.7的[笔趣看](http://www.biqukan.com/)小说网站爬取
本爬虫主要用于服务器使用，所以返回数据均为json

## 如何使用
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

### index 首页信息json说明
    {
        items： --最上面的4个推荐<br/>
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
    
### book_info 小说信息json说明 
    {
        "status": "连载", --小说状态
        "update_time": "2018-02-06 17:50:00", -- 更新时间
        "description": "一念成沧海，一念化桑田。一念斩千魔，一念诛万仙。唯我念……永恒", --小说描述、简介
        "chapters": [ --所有章节
            {
                "url": "5386269", --章节id、章节地址
                "title": "外传1 柯父。" --章节标题
            }
        ],
        "word_count": "3672172", --小说字数
        "title": "一念永恒", --小说标题
        "author": "耳根", --小说作者
        "cover": "http://www.biqukan.com/files/article/image/1/1094/1094s.jpg", --小说封面
        "update_url": "17930894", --最新章节地址
        "type": "玄幻小说", --小说类型
        "update_chapter": "第1307章 起源" --小说最新章节标题
    }

### chapter_info 小说章节json信息说明 
    {
        "title": "第1305章 逆陨", --章节标题
        "text_list": [  --章节内容list
            "　　第二指，无声无息点出的瞬间，白小纯的头发直接就花白了一半，他的皮肤也似乎失去了光泽，他的生命，他的生机在这一刹那消失，化作了无形之力，去与星空大道共鸣，去与那永恒本源形成的玄妙共鸣！",
            "　　就算是这样，它那看似无尽的生机，也都被吸走了只剩一丝，才可以让白小纯，加上自己的余力，展开第四指！",
            "　　此刻在这第四指下，星空波澜不起，白小纯疲惫中，眼睛慢慢闭上，似没有睁开的力气，他的身体也失去了支撑，向着永恒仙域的方向，慢慢的飘落……在他双眼闭合的瞬间，灭圣发出前所未有的嘶吼。"
        ],
        "list": "1_1094", --章节目录
        "next": “17927946", --下一章节
        "text": "　　第二指，，入的黑芒，使得其身体外这一瞬，的飘落……在他双眼闭合的瞬间，灭圣发出前所未有的嘶吼。", --章节内容文字
        "previous": "17916686" --上一章节
    }
    
### index_type 小说类型json说明 
    同indexjson

### query 小说查询json说明
    [
        {
            "status": "",
            "update_time": "2017-10-05",  --小说更新时间
            "description": "万界融合,灵力消散,……",  --小说描述
            "word_count": "",
            "title": "五行天",  --小说标题
            "url": "0_2",  --小说地址/id
            "author": "方想",  --小说作者
            "cover": "http://www.biqukan.com/files/article/image/0/2/2s.jpg",  --小说封面
            "update_url": "16239233",  --最新章节地址
            "type": "玄幻小说",  --小说类型
            "update_chapter": "第六百五十章这是什么剑术？"  --最新章节标题
        }
    ]

### ranking  小说排行榜json说明
    [
        {
            "list": [
                {
                    "url": "20_20623",  --小说地址/id
                    "type": "科幻小说",  --小说类型
                    "number": "1",  --小说排行
                    "title": "幻游猎人"  --小说标题
                }
        ],
        "title": "小说总榜"  --排行榜标题
        },
    ]
    
### 下载单个章节
    同小说章节信息