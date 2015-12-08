import xml.etree.ElementTree as ET
import json
import logging

from ETL.E.G1.authors import Authors
from ETL.E.G2.request.find_request import FindRequest
from ETL.E.G2.request.present_request import PresentRequest
from ETL.T.transformer import Transformer

logging.basicConfig()

authors = Authors()
authors.add_from_xml("data/000 - 999.xml")

aleph_data = ET.fromstring("<aleph></aleph>")

cnt = 0
for author in authors:
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

aleph_xml = ET.ElementTree()
aleph_xml._setroot(aleph_data)


print "---ALEPH WORK---"
with open("config/config_aleph_work.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/", "varfield[@id='245']/subfield[@label='a']",
                {"dct": "http://purl.org/dc/terms/", "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                 "ex": "http://example.com/"}
                )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph_work.ttl", format='turtle')

print "---ALEPH AUTHORITY---"
with open("config/config_aleph_authority.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/", "varfield[@id='100']/subfield[@label='a']",
                {"foaf": "http://xmlns.com/foaf/0.1/", "dct": "http://purl.org/dc/terms/",
                 "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "ex": "http://example.com/"}
                )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph_authority.ttl", format='turtle')

print "---MCH AUTHORITY---"
xml = ET.parse("data/000 - 999.xml")
with open("config/config_mch_authority.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/autoridad/", "property/property-value[@pnid='551']",
                {"foaf": "http://xmlns.com/foaf/0.1/", "dct": "http://purl.org/dc/terms/",
                 "rdfs": "http://www.w3.org/2000/01/rdf-schema#"}
                )
g = t.transform(xml)
g.serialize(destination="output/output_mch_authority.ttl", format='turtle')

print "---MCH WORK---"
xml = ET.parse("data/000 - 999.xml")
with open("config/config_mch_work.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/obra/", "name",
                {"foaf": "http://xmlns.com/foaf/0.1/", "dct": "http://purl.org/dc/terms/",
                 "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "ex": "http://example.com/"}
                )
g = t.transform(xml)
g.serialize(destination="output/output_mch_work.ttl", format='turtle')

print "---MCH BIBLIOGRAPHIC RESOURCE---"
xml = ET.parse("data/000 - 999.xml")
with open("config/config_mch_br.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/recurso_bibliografico/", "name",
                {"foaf": "http://xmlns.com/foaf/0.1/", "dct": "http://purl.org/dc/terms/",
                 "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "ex": "http://example.com/"}
                )
g = t.transform(xml)
g.serialize(destination="output/output_mch_br.ttl", format='turtle')

print "---MCH CATEGORY---"
xml = ET.parse("data/000 - 999.xml")
with open("config/config_mch_cat.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/categoria/", "properties/property/property-value[@pnid='522']",
                {"foaf": "http://xmlns.com/foaf/0.1/", "dct": "http://purl.org/dc/terms/",
                 "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "ex": "http://example.com/"}
                )
g = t.transform(xml)
g.serialize(destination="output/output_mch_cat.ttl", format='turtle')

print "---MCH THEME---"
xml = ET.parse("data/000 - 999.xml")
with open("config/config_mch_tema.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/tema/", "properties/property/property-value[@pnid='525']",
                {"foaf": "http://xmlns.com/foaf/0.1/", "dct": "http://purl.org/dc/terms/",
                 "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "ex": "http://example.com/"}
                )
g = t.transform(xml)
g.serialize(destination="output/output_mch_tema.ttl", format='turtle')