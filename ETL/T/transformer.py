import rdflib as rdf
import xml.etree.ElementTree as ET

class Transformer(object):
    def __init__(self, config, prefixes={}):
        assert isinstance(config, dict), \
            "config must be a dictionary: %r" % config
        assert isinstance(prefixes, dict), \
            "prefixes must be a dictionary: %r" % prefixes
        self.config = config
        self.prefixes = prefixes

    def transform(self, xml_data):
        """
        Transform the data using an specific configuration
        :param xml_data: xml element to transform
        :return: data graph in rdf format
        """
        assert isinstance(xml_data, ET.ElementTree), \
            "xml_data must be an instance of xml.etree.ElementTree: %r" % xml_data
        graph = rdf.Graph()
        keys = self.config.keys()
        for xpath in keys:
            values = xml_data.findall(xpath)
            for value in values:
                subject = rdf.BNode()
                prefix = self.prefixes[self.config[xpath]["prefix"]]
                predicate = rdf.term.URIRef(prefix + self.config[xpath]["property"])
                literal = rdf.Literal(value.text)
                graph.add((subject, predicate, literal))
        return graph