# from bs4 import BeautifulSoup
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def start(self, root_url):
        self.urls.add_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            try:
                html_cont = self.downloader.download(new_url)

                new_urls, new_data_list = self.parser.parse(new_url, html_cont)
                # self.urls.add_urls(new_urls)
                self.outputer.collect_data(new_data_list)
            except:
                print('fail:' + new_url)

        self.outputer.ouput_html()
        print('finish.')

print(__name__)
if __name__ == '__main__':
    print('start.')
    root_url = 'https://www.imooc.com/search/course?words=python'
    spider = SpiderMain()
    spider.start(root_url)
