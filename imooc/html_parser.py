from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


class HtmlParser(object):
    def _get_new_urls(self, url, soup):
        url_list = set()
        #<div class="page"><a>首页</a><a>上一页</a><a>1</a>
        #<a href="javascript:void(0)" class="active text-page-tag">2</a><span class="disabled_page">下一页</span><span class="disabled_page">尾页</span></div>
        active_link = soup.find('a', class_='active text-page-tag')
        next_link = active_link.next_sibling

        #下一页有效时候，追加
        if(''.join(next_link.get('class')) == 'text-page-tag'):
            new_url = urljoin(url, next_link.get('href'))
            url_list.add(new_url)

        return url_list

    def _get_new_data(self, url, soup):
        new_data_list = []

        item_list = soup.find_all('div', class_='course-item-detail')
        for item in item_list:
            new_data = {}

            node_title = item.find('a')
            new_data['title'] = node_title.get_text().strip()
            new_data['url'] = urljoin(url, node_title.get('href'))

            #<div class="course-item-classify"><span>实战</span><span>张三讲师</span><span>高级</span><span>4567</span>
            detail_types = item.find(
                'div', class_='course-item-classify').find_all('span')

            the_type = detail_types[0].get_text()
            the_grade = detail_types[2].get_text()
            the_play_count = detail_types[3].get_text()

            new_data['type'] = the_type.strip()
            new_data['grade'] = the_grade.strip()
            new_data['play_count'] = the_play_count.strip()

            new_data_list.append(new_data)

        return new_data_list

    def parse(self, url, content):
        if url is None or content is None:
            return None

        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data_list = self._get_new_data(url, soup)

        return new_urls, new_data_list
