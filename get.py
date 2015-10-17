from request.find_request import FindRequest
from request.present_request import PresentRequest

# TODO: Como lo haremos para todas las autoridades? encapsulamos esto en una clase person_etl?
author = 'Cortazar, Julio'  # sys.argv[1]

url = 'http://www.bncatalogo.cl/X'
config = {
    'code': 'wau',
    'base': 'BNC01'
}
request = FindRequest(base_url=url, config=config)
metadata = request.find(name=author)

# no_records = d['no_records']
no_entries = metadata['no_entries']
author_id = metadata['set_number']

request = PresentRequest(base_url=url, config=config, no_entries=no_entries)
# Here we should create a new rdf_graph with some library or by ourselves
# For example: an authority graph class for these
rdf_graph = ''  # authority_graph
while request.remain_data:
    author_data = request.get_chunk(author_id=author_id)
    # Somehow add the data to the graph
    rdf_graph.add(author_data)
    # If the data crosses some threshold, flush it
    # IMPORTANT NOTE: probably a single authority cant cause run out the memory
    # maybe this is needed in an upper level
    if rdf_graph.fullMemory():
        rdf_graph.writetoTTL()
# Last flush
rdf_graph.writetoTTL()

