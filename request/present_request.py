from request import Request
import xml.etree.ElementTree as _Et


class PresentRequest(Request):
    def __init__(self, base_url='', config={}, no_entries=0):
        super(PresentRequest, self).__init__(base_url, config)
        self.config['op'] = 'present'
        self.no_entries = no_entries
        self.chunk_size = 100
        self.current_entry = 1
        self.next_entry = min(self.no_entries, self.chunk_size)
        self.config['set_entries'] = str(self.current_entry) + '-' + str(self.next_entry)


    def get_chunk(self, author_id):
        # TODO: Maybe throw error when no data remains
        self.config['set_number'] = author_id
        print self.config
        # TODO: no funciona esta wea, me tira un xml todo mula
        response = self.send()
        print response.content
        xml = _Et.fromstring(response.content)
        data = {}
        for child in xml:
            if child.tag in ('error', 'session-id'):
                continue
            data[child.tag] = child.text
        self.current_entry = min(self.no_entries, self.current_entry + self.chunk_size)
        self.next_entry += self.chunk_size
        return data

    def remain_data(self):
        return self.current_entry == self.no_entries