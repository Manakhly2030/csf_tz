import xmltodict


def parse_xml(path):
    with open(path, "r") as f:
        xml = f.read()
    return xmltodict.parse(xml)
