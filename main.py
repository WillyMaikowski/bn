from ETL.T.transformer import Transformer
import xml.etree.ElementTree as ET
import json
import logging

logging.basicConfig()

xml = ET.parse("data/000 - 999.xml")
with open("config.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/", "article/properties/property/property-value[@pnid='551']", {"foaf": "http://xmlns.com/foaf/0.1/"})
g = t.transform(xml)

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print(s, p, o)