# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


class Authors(object):
    def __init__(self):
        self.names = {}

    def add_from_xml(self, filename):
        """
        Adds authors from an XML with an specific structure.
        :param filename: name of the XML file.
        """
        for event, elem in ET.iterparse(filename, events=('start', 'end', 'start-ns', 'end-ns')):
            if event != 'end':
                continue
            if elem.tag == 'property-value' and elem.get('pnid') == '551':
                name = elem.get('name')
                if name not in self.names:
                    self.names[name] = 0
                self.names[name] += 1

    def __str__(self):
        return str(self.names.keys())

    def __len__(self):
        return len(self.names)
