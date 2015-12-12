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
total = 20
for author in authors:
    cnt += 1
    if cnt == total:
        break
    print "Loading authors: " + str(100*cnt/total) + "%"
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
print "Authors 100% loaded."
aleph_xml = ET.ElementTree()
aleph_xml._setroot(aleph_data)

def preprocess_aleph(xml):
    base_xpath = "present/record/metadata/oai_marc/"
    name_xpath = base_xpath + "varfield[@id='100']/subfield[@label='a']"
    org_xpath = base_xpath + "varfield[@id='110']/subfield[@label='a']"
    title_xpath = base_xpath + "varfield[@id='245']/subfield[@label='a']"
    nick_xpath = base_xpath + "varfield[@id='245']/subfield[@label='c']"
    alternative_xpath = base_xpath + "varfield[@id='246']/subfield[@label='a']"
    references_xpath = base_xpath + "varfield[@id='600']/subfield[@label='a']"
    contributor_xpath = base_xpath + "varfield[@id='700']/subfield[@label='a']"
    br1_xpath = base_xpath + "varfield[@id='856']/subfield[@label='a']"
    br2_xpath = base_xpath + "varfield[@id='856']/subfield[@label='d']"
    br3_xpath = base_xpath + "varfield[@id='856']/subfield[@label='f']"
    br_uri1 = xml.findall(br1_xpath)
    br_uri2 = xml.findall(br2_xpath)
    br_uri3 = xml.findall(br3_xpath)
    br_uri_largo = len(br_uri1)
    for i in range(0, br_uri_largo-1):
        br_uri1[i].text = br_uri1[i].text + br_uri2[i].text + br_uri3[i].text
        br_uri3[i].text = br_uri3[i].text.replace(".","_")
    for elem in xml.findall(name_xpath):
        elem.text = elem.text.replace(".","")
        if elem.text[-1] == ",":
            elem.text = elem.text[0:len(elem.text)-1]
        name_parts = elem.text.split(", ")
        if len(name_parts) == 2:
            elem.text = name_parts[1] + " " + name_parts[0]
    for elem in xml.findall(org_xpath):
        if elem.text[-1] == ".":
            elem.text = elem.text[0:len(elem.text)-1]
    for elem in xml.findall(title_xpath):
        if elem.text[-1] == "/" or elem.text[-1] == ":":
            elem.text = elem.text[0:len(elem.text)-1]
        elem.text = elem.text.strip()
    for elem in xml.findall(nick_xpath):
        elem.text = elem.text.replace(".","")
        if elem.text[-1] == ".":
            elem.text = elem.text[0:len(elem.text)-1]
    # for elem in xml.findall(alternative_xpath):
    for elem in xml.findall(references_xpath):
        elem.text = elem.text.replace(".","")
        if elem.text[-1] == ",":
            elem.text = elem.text[0:len(elem.text)-1]
        name_parts = elem.text.split(", ")
        if len(name_parts) == 2:
            elem.text = name_parts[1] + " " + name_parts[0]
    for elem in xml.findall(contributor_xpath):
        elem.text = elem.text.replace(".","")
        if elem.text[-1] == ",":
            elem.text = elem.text[0:len(elem.text)-1]
        name_parts = elem.text.split(", ")
        if len(name_parts) == 2:
            elem.text = name_parts[1] + " " + name_parts[0]
    return xml

print "Preprocessing Aleph..."
aleph_xml = preprocess_aleph(aleph_xml)
print "Preprocess completed."

### ET FROM ALEPH ###
# Person Output
with open("config/config_aleph_person.json", "r") as fp:
   config = json.load(fp)
t = Transformer(config, "http://datos.bn.cl/recurso/persona/",
                "varfield[@id='100']/subfield[@label='a']",
                {"foaf": "http://xmlns.com/foaf/0.1/", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "lib": "http://datos.bn.cl"}
               )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph_person.ttl", format='turtle')
print "Person loaded to TTL."
# Organization Output
with open("config/config_aleph_organization.json", "r") as fp:
   config = json.load(fp)
t = Transformer(config, "http://datos.bn.cl/recurso/institucion/",
                "varfield[@id='110']/subfield[@label='a']",
                {"foaf": "http://xmlns.com/foaf/0.1/", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "lib": "http://datos.bn.cl/"}
               )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph_organization.ttl", format='turtle')
print "Organization loaded to TTL."
# CreativeWork Output
with open("config/config_aleph_creativework.json", "r") as fp:
   config = json.load(fp)
t = Transformer(config, "http://datos.bn.cl/recurso/obra/",
                "varfield[@id='245']/subfield[@label='a']",
                {"foaf": "http://xmlns.com/foaf/0.1/", "rdfs": "http://www.w3.org/2000/01/rdf-schema#", "lib": "http://datos.bn.cl/", "dct": "http://purl.org/dc/terms/"}
               )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph_creativework.ttl", format='turtle')
print "CreativeWork loaded to TTL."
# Collection Output
with open("config/config_aleph_collection.json", "r") as fp:
   config = json.load(fp)
t = Transformer(config, "http://datos.bn.cl/recurso/tema/",
                "varfield[@id='650']/subfield[@label='a']",
                {"rdfs": "http://www.w3.org/2000/01/rdf-schema#", "lib": "http://datos.bn.cl/", "dct": "http://purl.org/dc/terms/"}
               )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph_collection.ttl", format='turtle')
print "Collection loaded to TTL."
# BibliographicResource Output
with open("config/config_aleph_br.json", "r") as fp:
   config = json.load(fp)
t = Transformer(config, "http://datos.bn.cl/recurso/material_digital/",
                "varfield[@id='856']/subfield[@label='f']",
                {"rdfs": "http://www.w3.org/2000/01/rdf-schema#", "lib": "http://datos.bn.cl/", "dct": "http://purl.org/dc/terms/"}
               )
g = t.transform(aleph_xml)
g.serialize(destination="output/output_aleph_br.ttl", format='turtle')
print "BibliographicResource loaded to TTL."

### ET FROM MCH ###
'''
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
'''
