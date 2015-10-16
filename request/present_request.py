from request import Request
import xml.etree.ElementTree as _et


class PresentRequest(Request):
    name = ""
    set_number = -1
    no_records = -1
    no_entries = -1

    def __init__(self, base_url="", config=""):
        super(PresentRequest, self).__init__(base_url, config)
        self.config['op'] = 'find'

    def get_chunk(self, name=None, base_url=None, config=None):
        # tbd
        return


'''
entregar name -> buscar -> obtener metadatos
-> obtener un chunk de los datos (maximo 100)
-> saber cuantos datos tengo que sacar ->
iterar hasta que no queden pedazos de informacion
-> saber escribir cada pedazo obtenido (los chunk retornar xmls)
'''
