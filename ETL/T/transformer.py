import rdflib as rdf
import xml.etree.ElementTree as ET
from unidecode import unidecode


class Transformer(object):
    def __init__(self, config, resource_uri, uri_identifier='', prefixes={}):
        assert isinstance(config, dict), \
            "config must be a dictionary: %r" % config
        assert isinstance(resource_uri, str), \
            "resource_uri must be a string: %r" % resource_uri
        assert isinstance(uri_identifier, str), \
            "uri_identifier must be a string: %r" % uri_identifier
        assert isinstance(prefixes, dict), \
            "prefixes must be a dictionary: %r" % prefixes
        self.config = config
        self.resource_uri = resource_uri
        self.uri_identifier = uri_identifier
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
        xpaths.remove("loop")

        author_elements = xml_data.findall(self.config["loop"])
        values = []
        for element in author_elements:
            a_list = []
            for xpath in xpaths:
                value = element.find(xpath)
                if value is None:
                    continue
                a_list.append(value)
            values.append(a_list)

        resource_id = xpaths.index(self.uri_identifier)

        for i in range(len(values)):
            for j in range(len(values[i])):
                if "&lt;" in values[i][resource_id].text:
                    continue
                subject = rdf.URIRef(
                    unidecode(
                        unicode(
                            self.resource_uri +
                            values[i][resource_id].text.replace(" ", "_").replace("\"", "")
                        )
                    )
                )
                prefix = self.prefixes[self.config[xpaths[j]]["prefix"]]
                predicate = rdf.term.URIRef(prefix + self.config[xpaths[j]]["property"])
                literal = rdf.Literal(values[i][j].text)
                graph.add((subject, predicate, literal))

        return graph