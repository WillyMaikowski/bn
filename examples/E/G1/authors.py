from ETL.E.G1.authors import Authors
import os

authors = Authors()
for dirpath, dnames, fnames in os.walk("./mch/"):
    for f in fnames:
        if f.endswith(".xml"):
            print os.path.join(dirpath, f)
            authors.add_from_xml(os.path.join(dirpath, f))

authors.add_from_xml(2)
# print authors
# print '*** Numero de autores ***'
print len(authors)
