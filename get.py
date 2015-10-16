import requests as _r
import xml.etree.ElementTree as _et
import xml.dom.minidom
import sys

# Correr el script desde la linea de comandos, poniendo como parametro al autor.
# Por ejemplo: python get.py "Cortazar, Julio"

autor = sys.argv[1]
url = 'http://www.bncatalogo.cl/X'
output = 'autoridad_' + autor.replace(', ','_') + '.xml'

print 'Obteniendo XML de ' + autor
config = {
    'op': 'find',
    'code': 'wau',
    'request': autor,
    'base': 'BNC01'
}

res = _r.get( url, params = config )
res.raise_for_status()

xml = _et.fromstring( res.content )
d = {}
for child in xml:
    if child.tag in ( 'error', 'session-id' ): continue
    #set_number, no_records, no_entries
    d[child.tag] = int(child.text)

#si no hay coincidencias con find, se abandona el script
if len(d) == 0:
    print('Error: Busqueda infructuosa.')
    sys.exit()
print d

# por lo que se ve, hay que usar el numero de entries
#no_records = d['no_records']
no_entries = d['no_entries']
set_number = d['set_number']
i = 1
bad_words = []
# resetear el output en caso de existir
open(output, 'w').close()
newfile = open(output, 'a');
# realizar ciclo que recupere de 100 en 100 los registros
while i <= no_entries+99:
    config = {
        'op': 'present',
        'set_entry': str(i)+'-'+str(i+99),
        'set_number': set_number
    }
    res = _r.get( url, params = config )
    res.raise_for_status()
    text_data = res.content
    #text_file = open('temporal.xml', 'w')
    #text_file.write(res.content)
    #text_file.close()
    # filtrar palabras no deseadas para no ser incluidas en el xml
    if i == 1:
        bad_words = ['<session-id>', '</present>', '<error>']
    else:
        bad_words = ['<?xml', '<present>', '<session-id>', '</present>', '<error>']
    # escribir en el output desde el archivo temporal
    for line in text_data.splitlines():
        if line != ' ' and not any(bad_word in line for bad_word in bad_words):
            newfile.write(line+'\n')
    '''
    with open('temporal.xml','r') as oldfile, open(output, 'a') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
    '''
    i += 100
# escribir ultima linea del output
newfile.write('</present>')
newfile.close()

'''
Intento de prettificar
new_xml = xml.dom.minidom.parse(output) # or xml.dom.minidom.parseString(xml_string)
pretty_xml = xml.toprettyxml()
text_file = open(output + '_pretty.xml', 'w')
text_file.write()
text_file.close()
'''

print('Listo!')

