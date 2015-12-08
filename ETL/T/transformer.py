import xml.etree.ElementTree as ET

import rdflib as rdf
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
        if "$EXTRA" in self.config:
            xpaths.remove("$EXTRA")

        author_elements = xml_data.findall(self.config["loop"])
        values = []
        for element in author_elements:
            a_list = []
            for xpath in xpaths:
                value = element.find(xpath)
                # if value is None:
                #    continue
                a_list.append((self.config[xpath], value))
            if len(a_list) == 0:
                continue
            values.append(a_list)

        resource_id = xpaths.index(self.uri_identifier)

        for i in range(len(values)):
            if values[i][resource_id][1] is None:
                continue
            if "&lt;" in values[i][resource_id][1].text:
                continue
            if "^" in values[i][resource_id][1].text:
                continue
            if "[" in values[i][resource_id][1].text:
                continue
            for j in range(len(values[i])):
                if values[i][j][1] is None:
                    continue
                subject = rdf.URIRef(
                    unidecode(
                        unicode(
                            self.resource_uri +
                            values[i][resource_id][1].text.strip().replace(" ", "_").replace("\"", "")
                        )
                    )
                )
                prefix = self.prefixes[values[i][j][0]["prefix"]]
                predicate = rdf.term.URIRef(prefix + values[i][j][0]["property"])
                if "class_uri" in values[i][j][0]:
                    resource_uri = unidecode(
                        unicode(
                            values[i][j][0]["class_uri"] + values[i][j][1].text.strip().replace(" ", "_").replace("\"", "")
                        )
                    )
                    '''
                    TODO: HACK para quitar la coma final. En aleph los nombres de los autores salen con una coma final,
                    en mch no. Deberia resolverse de otro modo
                    '''
                    if resource_uri[-1] == ",":
                        resource_uri = resource_uri[0:len(resource_uri)-1]
                    resource_object = rdf.term.URIRef(resource_uri)
                else:
                    resource_object = rdf.Literal(values[i][j][1].text.strip())
                graph.add((subject, predicate, resource_object))
            if "$EXTRA" in self.config:
                for extra in self.config["$EXTRA"]:
                    subject = rdf.URIRef(
                        unidecode(
                            unicode(
                                self.resource_uri +
                                values[i][resource_id][1].text.strip().replace(" ", "_").replace("\"", "")
                            )
                        )
                    )
                    prefix = self.prefixes[extra["prefix"]]
                    predicate = rdf.term.URIRef(prefix + extra["property"])
                    resource_object = rdf.term.URIRef(self.prefixes[extra["value"]["prefix"]] + extra["value"]["property"])
                    graph.add((subject, predicate, resource_object))

        return graph