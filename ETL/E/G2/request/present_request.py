from request import Request
import xml.etree.ElementTree as _Et


class PresentRequest(Request):
    def __init__(self, base_url='', no_entries=0, author_id=''):
        super(PresentRequest, self).__init__(base_url, {})
        self.config['op'] = 'present'
        self.config['set_number'] = author_id
        self.no_entries = no_entries
        self.chunk_size = 100
        self.current_entry = 1
        self.next_entry = min(self.no_entries, self.chunk_size)
        self.config['set_entry'] = str(self.current_entry) + '-' + str(self.next_entry)

    def get_chunk(self):
        """
        Gets the next data chunk of the author.
        :return: An xml.etree.ElementTree object with the data.
        """
        # TODO: Maybe throw error when no data remains
        response = self.send()
        xml = _Et.fromstring(response.content)
        self.current_entry = min(self.no_entries + 1, self.current_entry + self.chunk_size)
        self.next_entry = min(self.no_entries, self.next_entry + self.chunk_size)
        self.config['set_entry'] = str(self.current_entry) + '-' + str(self.next_entry)
        return xml

    def remain_data(self):
        """
        Checks if remains data to get in the request.
        :return: True if data remains, false otherwise.
        """
        return self.current_entry <= self.no_entries
