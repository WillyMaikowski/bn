from ETL.E.G2 import FindRequest

url = 'http://www.bncatalogo.cl/X'

request = FindRequest(base_url=url)
request = request.find(name='Cortazar, Julio')
print request
