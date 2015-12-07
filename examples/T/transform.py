from ETL.T.transformer import Transformer
import xml.etree.ElementTree as ET

xml = ET.parse("sample.xml")
config = {"book/author": {"prefix": "foaf", "property": "name"}, "book/title": {"prefix": "foaf", "property": "primaryTopic"}}
t = Transformer(config, "http://example.com/", "book/author", {"foaf": "http://xmlns.com/foaf/0.1/"})
g = t.transform(xml)

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print(s, p, o)
