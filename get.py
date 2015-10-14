import requests as _r
import xml.etree.ElementTree as _et

url = 'http://www.bncatalogo.cl/X'
config = {
    'op': 'find',
    'code': 'wau',
    'request': 'Neruda',
    'base': 'BNC01'
}

res = _r.get( url, params = config )
res.raise_for_status()

xml = _et.fromstring( res.content )
d = {}
for child in xml:
    if child.tag in ( 'error', 'session-id' ): continue
    #set_number, no_records, no_entries
    d[child.tag] = int( child.text )

print d










'''
# version para respuestas largas (?)
res.raw.decode_content = True
events = _et.iterparse( res.raw )
for elem, event in events:
    print elem
'''

