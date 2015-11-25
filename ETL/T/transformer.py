import rdflib as rdf
import xml.etree.ElementTree as ET

class Transformer(object):
    def __init__(self, config, resource_uri, prefixes={}):
        assert isinstance(config, dict), \
            "config must be a dictionary: %r" % config
        assert isinstance(resource_uri, str), \
            "resource_uri must be a string: %r" % resource_uri
        assert isinstance(prefixes, dict), \
            "prefixes must be a dictionary: %r" % prefixes
        self.config = config
        self.resource_uri = resource_uri
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
        xpaths = self.config.keys()
        values = []
        for xpath in xpaths:
            values.append(xml_data.findall(xpath))
        counter = 0
        for i in range(len(values[0])):
            subject = rdf.URIRef(self.resource_uri + str(counter))
            for j in range(len(values)):
                prefix = self.prefixes[self.config[xpaths[j]]["prefix"]]
                predicate = rdf.term.URIRef(prefix + self.config[xpaths[j]]["property"])
                literal = rdf.Literal(values[j][i].text)
                graph.add((subject, predicate, literal))
            counter += 1
        return graph
