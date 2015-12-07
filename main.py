from ETL.E.G1.authors import Authors
from ETL.E.G2.request.find_request import FindRequest
from ETL.E.G2.request.present_request import PresentRequest
from ETL.T.transformer import Transformer
import xml.etree.ElementTree as ET
import json
import logging


logging.basicConfig()

authors = Authors()
authors.add_from_xml("data/000 - 999.xml")

print len(authors)
aleph_data = ET.fromstring("<aleph></aleph>")

cnt = 0
for author in authors.names.keys():
    cnt += 1
    if cnt == 2:
        break
    url = 'http://www.bncatalogo.cl/X'
    request = FindRequest(base_url=url)
    metadata = request.find(name=author)

    if len(metadata.keys()) == 0:
        logging.warning("Author '" + author + "' not found.")
        continue

    no_entries = metadata['no_entries']
    author_id = metadata['set_number']
    request = PresentRequest(base_url=url, no_entries=no_entries, author_id=author_id)

    author_data = []
    while request.remain_data():
        author_data.append(request.get_chunk())

    for elem in author_data:
        aleph_data.append(elem)

print "DONE"
aleph_xml = ET.ElementTree()
aleph_xml._setroot(aleph_data)

aleph_xml.write("stuff.xml")

with open("config/config_aleph.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/",
                "varfield[@id='245']/subfield[@label='a']",
                {"dct": "http://purl.org/dc/terms/"}
                )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph.ttl", format='turtle')

xml = ET.parse("data/000 - 999.xml")
with open("config/config_mch.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/", "property/property-value[@pnid='551']", {"foaf": "http://xmlns.com/foaf/0.1/"})
g = t.transform(xml)
g.serialize(destination="output/output_mch.ttl", format='turtle')