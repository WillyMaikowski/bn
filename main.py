from ETL.E.G2.request.find_request import FindRequest
from ETL.E.G1.authors import Authors
import os

authors = Authors()
# authors.addFromXML('mch/000 - 999.xml')
# Dejo comentada esta parte, pues con todos los archivos que hay, el proceso es algo lento.
for dirpath, dnames, fnames in os.walk("./mch/"):
    for f in fnames:
        if f.endswith(".xml"):
            print os.path.join( dirpath, f )
            authors.addFromXML( os.path.join( dirpath, f ) )

#print authors
#print '*** Numero de autores ***'
print len( authors )

'''
url = 'http://www.bncatalogo.cl/X'
request = FindRequest(base_url=url)
request = request.find(name='Cortazar, Julio')
print request
'''
