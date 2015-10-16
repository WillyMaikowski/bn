from find_request import find_request

url = 'http://www.bncatalogo.cl/X'
config = {
    'code': 'wau',
    'base': 'BNC01'
}
request = find_request( base_url = url, config = config)
request = request.find(name = "raul")
print request
