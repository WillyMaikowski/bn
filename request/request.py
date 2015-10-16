import requests as r


class Request(object):
    def __init__(self, base_url, config):
        self.base_url = base_url
        self.config = config

    def send(self):
        return r.get(self.base_url, params=self.config)

    def set_config(self, config):
        self.config = config

    def set_base_url(self, base_url):
        self.base_url = base_url
