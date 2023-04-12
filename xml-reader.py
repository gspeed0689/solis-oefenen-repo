from xml.dom import minidom

def open_xml(filename):
    f = open(filename, "r")
    xmldoc = minidom.parseString(f.read())
    return(xmldoc)