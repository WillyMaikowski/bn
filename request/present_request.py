from request import Request


class PresentRequest(Request):
    def __init__(self, base_url='', config='', no_entries=0):
        super(PresentRequest, self).__init__(base_url, config)
        self.config['op'] = 'present'
        self.no_entries = no_entries
        self.chunk_size = 100
        self.current_entry = 1
        self.next_entry = max(no_entries, self.chunk_size)
        self.config['set_entries'] = str(self.current_entry) + '-' + str(self.current_entry)


    def get_chunk(self, author_id):
        self.config['set_number'] = author_id
        # tbd
        # TODO: get the stuff
        self.current_entry += self.chunk_size
        self.next_entry += self.chunk_size

    def remain_data(self):
        return self.current_entry == self.no_entries

'''
entregar name -> buscar -> obtener metadatos
-> obtener un chunk de los datos (maximo 100)
-> saber cuantos datos tengo que sacar ->
iterar hasta que no queden pedazos de informacion
-> saber escribir cada pedazo obtenido (los chunk retornar xmls)
'''
# TODO: this should go somehow to the present request
    # config = {
    #    'op': 'present',
    #    'set_entry': str(i)+'-'+str(i+99),
    #    'set_number': set_number
    # }
    # res = _r.get( url, params = config )
    # res.raise_for_status()
    # text_data = res.content
    # text_file = open('temporal.xml', 'w')
    # text_file.write(res.content)
    # text_file.close()
    # filtrar palabras no deseadas para no ser incluidas en el xml
    # if i == 1:
    #    bad_words = ['<session-id>', '</present>', '<error>']
    # else:
    #    bad_words = ['<?xml', '<present>', '<session-id>', '</present>', '<error>']
    # escribir en el output desde el archivo temporal
    # for line in text_data.splitlines():
    #    if line != ' ' and not any(bad_word in line for bad_word in bad_words):
    #        newfile.write(line+'\n')
    '''
    with open('temporal.xml','r') as oldfile, open(output, 'a') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
    '''
    #i += 100
# escribir ultima linea del output
# newfile.write('</present>')
# newfile.close()

'''
Intento de prettificar
new_xml = xml.dom.minidom.parse(output) # or xml.dom.minidom.parseString(xml_string)
pretty_xml = xml.toprettyxml()
text_file = open(output + '_pretty.xml', 'w')
text_file.write()
text_file.close()
'''
