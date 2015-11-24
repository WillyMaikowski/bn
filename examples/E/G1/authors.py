from ETL.E.G1.authors import Authors
import os

authors = Authors()
for dirpath, dnames, fnames in os.walk("./mch/"):
    for f in fnames:
        if f.endswith(".xml"):
            print os.path.join(dirpath, f)
            authors.addFromXML(os.path.join(dirpath, f))

# print authors
# print '*** Numero de autores ***'
print len(authors)
