# -*- coding: utf-8 -*
import xml.etree.ElementTree as ET
import json

class Authors(object):
    def __init__(self):
        self.names = {}
        
    def addAuthorsFromXML(self, filename):
        for event, elem in ET.iterparse( filename, events=( 'start', 'end', 'start-ns', 'end-ns' ) ):
            if event != 'end': continue
            if elem.tag == 'property-value' and elem.get('pnid') == '551':
                name = elem.get('name')
                self.names.update({name:0})

    def showAuthors(self):
        return json.dumps(self.names, ensure_ascii=False)

    def countAuthors(self):
        return len(self.names)
