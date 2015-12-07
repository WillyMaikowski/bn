from request import Request
import xml.etree.ElementTree as _Et


class FindRequest(Request):
    def __init__(self, base_url=''):
        assert isinstance(base_url, str), \
            "base_url must be a string: %r" % base_url
        super(FindRequest, self).__init__(base_url, {})
        self.config['op'] = 'find'
        self.config['code'] = 'wau'
        self.config['base'] = 'BNC01'

    def find(self, name):
        """
        Gets the metadata for the author in name.
        :param name: String with author name. For example 'Cortazar, Julio'.
        :return: A dictionary with the respective metadata.
        """
        assert isinstance(name, str), \
            "name must be a string: %r" % name
        self.config['request'] = name
        response = self.send()
        xml = _Et.fromstring(response.content)
        d = {}
        for child in xml:
            if child.tag in ('error', 'session-id'):
                continue
            d[child.tag] = int(child.text)
        return d
