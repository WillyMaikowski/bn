from ETL.E.G2.request.find_request import FindRequest
from authors import Authors

authors = Authors()
authors.addAuthorsFromXML('Datos-MCH/000 - 999.xml')
# Dejo comentada esta parte, pues con todos los archivos que hay, el proceso es algo lento.
'''
i = 1000
while i < 27000:
    authors.addAuthorsFromXML('Datos-MCH/' + str(i) + ' - ' + str(i+999) + '.xml')
    i += 1000
    print i
authors.addAuthorsFromXML('Datos-MCH/28000 - 28371.xml')
'''
print authors.showAuthors()
print '*** Numero de autores ***'
print authors.countAuthors()

url = 'http://www.bncatalogo.cl/X'
request = FindRequest(base_url=url)
request = request.find(name='Cortazar, Julio')
print request
