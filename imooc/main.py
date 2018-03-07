# from bs4 import BeautifulSoup
import html_downloader
import html_outputer
import html_parser
import url_manager
from urllib.parse import urljoin, urlencode, quote_plus


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def getRootUrl(self, baseUrl, search):
        return urljoin(baseUrl, '?words=' + quote_plus(search))

    def start(self):
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            try:
                print('catch url: ', new_url)
                html_cont = self.downloader.download(new_url)

                new_urls, new_data_list = self.parser.parse(new_url, html_cont)
                self.urls.add_urls(new_urls)
                self.outputer.collect_data(new_data_list)
            except:
                print('fail:' + new_url)

        self.outputer.ouput_html()
        print('finish.')


print(__name__)
if __name__ == '__main__':
    print('start.')
    base_url = 'https://www.imooc.com/search/course'
    spider = SpiderMain()
    all_words = ['python', 'javascript', '前端',
                 'reactjs', '区块链', 'java', 'redis']

    for word in all_words:
        url = spider.getRootUrl(base_url, word)
        spider.urls.add_url(url)

    spider.start()
