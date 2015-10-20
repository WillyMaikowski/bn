import requests as r


class Request(object):
    def __init__(self, base_url, config):
        self.base_url = base_url
        self.config = config

    def send(self):
        response = r.get(self.base_url, params=self.config)
        response.raise_for_status()
        return response
