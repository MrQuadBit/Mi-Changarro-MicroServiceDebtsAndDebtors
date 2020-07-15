from lxml import etree

def validateXML(xml_parsed, dtd_name):
	#xml_file = etree.parse(xml_name)
	xml_validator = etree.DTD(dtd_name)

	return xml_validator.validate(xml_parsed)

def stringToXML(xml_string):

	return etree.fromstring(xml_string)
	
def xmlToString(xml):

	return etree.tostring(xml.getroot())

def fileToXML(xml_name):

	return etree.parse(xml_name)

def fileToString(xml_name):
	xml = fileToXML(xml_name)
	xml_string = xmlToString(xml)
	return xml_string
