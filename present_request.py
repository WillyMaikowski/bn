from request import request
import xml.etree.ElementTree as _et

class present_request(request):

	def __init__(self, base_url = "", config = ""):
		super(present_request, self).__init__(base_url,config)
		self.arg = arg
