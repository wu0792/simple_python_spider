class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data_list):
        if data_list is None:
            return

        self.datas.extend(data_list)

    def ouput_html(self):
        fout = open('./imooc/output.html', 'w', encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['type'])
            fout.write('<td>%s</td>' % data['grade'])
            fout.write('<td>%s</td>' % data['play_count'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()
