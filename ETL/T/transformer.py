import rdflib as rdf

class Transformer(object):
    def __init__(self, config):
        self.config = config

    def transform(self, xml_data):
        """
        Transform the data using an specific configuration
        :param xml_data: xml element to transform
        :return: data in rdf format
        """
        # rdf
        return xml_data