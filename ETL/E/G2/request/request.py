import requests as r


class Request(object):
    def __init__(self, base_url, config):
        assert isinstance(base_url, str), \
            "base_url must be a string: %r" % base_url
        assert isinstance(base_url, str), \
            "config must be a dictionary: %r" % config
        self.base_url = base_url
        self.config = config

    def send(self):
        """
        Sends the request and obtains a response
        :return: response of the request
        """
        response = r.get(self.base_url, params=self.config)
        response.raise_for_status()
        return response
