import requests as _r
import xml.etree.ElementTree as _et 

class request(object):
	base_url = ""
	config = ""

	def __init__(self,base_url,config):
		self.base_url = base_url
		self.config = config

	def send(self):
		return _r.get( self.base_url, params = self.config )