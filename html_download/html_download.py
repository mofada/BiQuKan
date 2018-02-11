# coding=utf-8
import urllib2

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}


class HtmlDownload(object):
    @staticmethod
    def download(url):
        # 判断url是否合法
        if url is None:
            return None
        try:
            # 开始请求
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)

            # 判断结果
            if response.getcode() != 200:
                return None

            # 返回结果
            return response.read()
        except Exception, e:
            print e.message + " : " + url
            return None
