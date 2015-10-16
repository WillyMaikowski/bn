import xml.etree.ElementTree as _et
import sys

for event, elem in _et.iterparse( 'temporal.xml', events=( 'start', 'end', 'start-ns', 'end-ns' ) ):
        print elem.text
