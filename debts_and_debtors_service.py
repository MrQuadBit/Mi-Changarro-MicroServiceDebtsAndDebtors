# Libraries
from flask import Flask, request, Response, render_template
from flask_cors import CORS
from lxml import etree
import xml_handler

# Constants
DB_PERSONS = "persons.xml"
DTD_PERSONS = "persons.dtd"

# MiChangarro's micro service (debts and debtors)
app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
	return render_template('cliente.html')


@app.route('/debts&debtors', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def debtsAndDebtors():
	if request.method == 'GET':
		print(request)
		response = xml_handler.fileToString(DB_PERSONS)
		return Response(response, status=200, mimetype="text/xml")
	elif request.method == 'POST':
		print(request)
		response = request.data
		#Handler for root syntax errors
		try:
			new_xml = xml_handler.stringToXML(response)
		except:
			return Response("XML received is invalid", status=400, mimetype="text/xml")
		is_valid = xml_handler.validateXML(new_xml, DTD_PERSONS)

		#Service's response
		service_response = etree.Element('response')
		if is_valid:
			service_response.text ="XML received successfuly"

			#Charging the DB in memory as xml_parsed
			xml_persons = xml_handler.fileToXML(DB_PERSONS)
			persons = xml_persons.getroot()

			#Adding received person
			if len(new_xml) > 0:
				persons.append(new_xml[0])
				xml_persons.write(DB_PERSONS)
			return Response(etree.tostring(service_response), status=201, mimetype="text/xml")
		else:
			service_response.text ="XML received is invalid"
			return Response(etree.tostring(service_response), status=400, mimetype="text/xml")
	elif request.method == 'DELETE':
		print(request)
		response = request.data
		#Handler for root syntax errors
		try:
			new_xml = xml_handler.stringToXML(response)
		except:
			return Response("XML received is invalid", status=400, mimetype="text/xml")
		is_valid = xml_handler.validateXML(new_xml, DTD_PERSONS)

		#Service's response
		#service_response = etree.Element('response')
		if is_valid:
			#Charging the DB in memory as xml_parsed
			xml_persons = xml_handler.fileToXML(DB_PERSONS)
			persons = xml_persons.getroot()

			#Deleting person received
			if len(new_xml) > 0:
				person_received_name = new_xml[0][0].text
				exists_person = False

				#searching person recieved in data base
				for person in persons:
					for name in person.iter('name'):
						if name.text == person_received_name:
							exists_person = True
							persons.remove(person)
							xml_persons.write(DB_PERSONS)
							break
					if exists_person:
						break

				if not exists_person:
					return Response("Person does not exists in data base", status=404, mimetype="text/xml")
				else:
					return Response("Person was removed successfuly", status=200, mimetype="text/xml")
		else:
			return Response("XML received is invalid", status=400, mimetype="text/xml")
	elif request.method == 'PATCH':
		print(request)
		response = request.data
		#Handle root syntax errors
		try:
			new_xml = xml_handler.stringToXML(response)
		except:
			return Response("XML received is invalid", status=400, mimetype="text/xml")

		is_valid = xml_handler.validateXML(new_xml, DTD_PERSONS)

		#Service's response
		if is_valid:
			#Charging DB in memory as xml_parsed
			xml_persons = xml_handler.fileToXML(DB_PERSONS)
			persons = xml_persons.getroot()

			#Patchin person
			if len(new_xml) > 0:
				existing_person = new_xml[0]
				new_person = new_xml[1]
				exists_person = False

				for person in persons:
					for name in person.iter('name'):
						if name.text == existing_person[0].text:
							exists_person = True
							person.set('type', new_person.attrib.pop('type'))
							person[0].text = new_person[0].text
							person[1].text = new_person[1].text
							xml_persons.write(DB_PERSONS)
							break
					if exists_person:
						break

				if not exists_person:
					return Response("Person does not exists in data base", status=404, mimetype="text/xml")
				else:
					return Response("Person was modified successfuly", status=200, mimetype="text/xml")
		else:
			return Response("XML recieved is invalid", status=200, mimetype="text/xml")

		return Response('This is a PATCH', status=200, mimetype="text/xml")



# Main
if __name__ == "__main__":
	#app.run(host='0.0.0.0', debug=True, port=4040)
	app.run(debug=True, port=4040)