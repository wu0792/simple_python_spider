class UrlManager(object):
    def __init__(self):
        self.old_list = set()
        self.new_list = set()

    def add_url(self, url):
        if url is None or url in self.old_list or url in self.new_list:
            return

        self.new_list.add(url)

    def add_urls(self, urls):
        if urls is None:
            return

        for url in urls:
            self.add_url(url)

    def has_new_url(self):
        return len(self.new_list) > 0

    def get_new_url(self):
        if len(self.new_list) == 0:
            return None

        new_url = self.new_list.pop()
        self.old_list.add(new_url)

        return new_url