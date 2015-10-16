from request import Request
import xml.etree.ElementTree as _Et


class FindRequest(Request):
    def __init__(self, base_url='', config=''):
        super(FindRequest, self).__init__(base_url, config)
        self.config['op'] = 'find'

    # busca al personaje "name" y retorna un diccionario con los datos respectivos
    # las variables base url y config son opcionales
    def find(self, name):
        self.config['request'] = name
        response = self.send()
        xml = _Et.fromstring(response.content)
        d = {}
        for child in xml:
            if child.tag in ('error', 'session-id'):
                continue
            d[child.tag] = int(child.text)
        return d
