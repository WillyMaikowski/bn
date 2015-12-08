import xml.etree.ElementTree as ET
import json

from ETL.T.transformer import Transformer

xml = ET.parse("sample.xml")
with open("config_mch_authority.json", "r") as fp:
    config = json.load(fp)
t = Transformer(config, "http://example.com/", "book/author", {"foaf": "http://xmlns.com/foaf/0.1/"})
g = t.transform(xml)

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print(s, p, o)
