from request.find_request import FindRequest
from request.present_request import PresentRequest

# TODO: Como lo haremos para todas las autoridades? encapsulamos esto en una clase person_etl?
author = "Neruda, Pablo"  # sys.argv[1]
output = 'authority_' + author.replace(', ','_') + '.xml'

url = 'http://www.bncatalogo.cl/X'
config = {
    'code': 'wau',
    'base': 'BNC01'
}
request = FindRequest(base_url=url, config=config)
metadata = request.find(name=author)

no_entries = metadata['no_entries']
author_id = metadata['set_number']
bad_words = []
# se setean los parametros para hacer el request
request = PresentRequest(base_url=url, no_entries=no_entries)
# resetear el output en caso de existir
open(output, 'w').close()
newfile = open(output, 'a');
# realizar ciclo que recupere de 100 en 100 los registros
while request.remain_data():
    # se obtiene un trozo del XML
    author_data = request.get_chunk(author_id=author_id)
    # filtrar palabras no deseadas para no ser incluidas en el xml
    if request.current_entry == 1:
        bad_words = ['<session-id>', '</present>', '<error>']
    else:
        bad_words = ['<?xml', '<present>', '<session-id>', '</present>', '<error>']
    # escribir en el output desde author_data
    for line in author_data.splitlines():
        if line != ' ' and not any(bad_word in line for bad_word in bad_words):
            newfile.write(line+'\n')
# Last flush
newfile.write('</present>')
newfile.close()
#rdf_graph.writetoTTL()

