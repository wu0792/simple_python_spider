from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParser(object):
    def _get_new_urls(self, url, soup):
        url_list = set()
        #/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6
        links = soup.find_all('a', href=re.compile(r'^/item/.*'))
        for link in links:
            new_url = urljoin(url, link['href'])
            url_list.add(new_url)
        return url_list

    def _get_new_data(self, url, soup):
        new_data = {}

        new_data['url'] = url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        node_title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        new_data['title'] = node_title.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        node_summary = soup.find('div', class_='lemma-summary')
        new_data['summary'] = node_summary.get_text()

        return new_data

    def parse(self, url, content):
        if url is None or content is None:
            return None

        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)

        return new_urls, new_data
