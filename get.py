import requests as _r
import xml.etree.ElementTree as _et
import sys

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

print res.raw

#si no hay coincidencias con find, se abandona el script
if len(d) == 0:
    print('Error: Busqueda infructuosa.')
    sys.exit()

#realizar ciclo que recupere de 100 en 100 los registros
set_number = d['set_number']
i = 1
while i <= set_number:
    if i%100 == 1:
        config = {
            'op': 'present',
            'set_entry': str(i)+'-'+str(i+99),
            'set_number': set_number
        }
        res = _r.get( url, params = config )
        res.raise_for_status()
        xml = _et.fromstring( res.content )
        print xml.child
    i = set_number





'''
# version para respuestas largas (?)
res.raw.decode_content = True
events = _et.iterparse( res.raw )
for elem, event in events:
    print elem
'''

