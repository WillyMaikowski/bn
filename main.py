from request.find_request import FindRequest

url = 'http://www.bncatalogo.cl/X'
config = {
    'code': 'wau',
    'base': 'BNC01'
}
request = FindRequest(base_url=url, config=config)
request = request.find(name="Cortazar, Julio")
print request
