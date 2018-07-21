__author__='pulidon'

import json
import requests


# datos de pruebas
url_pruebas_consultas = 'https://sandbox.api.payulatam.com/reports-api/rest/v4.9/'
url_pruebas_pagos = 'https://sandbox.api.payulatam.com/payments-api/rest/v4.9/'
url = url_pruebas_pagos
merchantid = ''
APIlogin = ''
APIKey = ''
accountId = ''
headers = {
	'POST /payments-api/4.0/service.cgi HTTP/1.1',
	'Host':'sandbox.api.payulatam.com',
	'Content-Type':'application/json; charset=utf-8',
	'Accept':'application/json',
	'Accept-language':'es',
	'Content-Length':'length',
	'Authorization': 'Basic ZDdBQWt4MThYTzg2RTAwOjg1TmU5RW80cjZDM1A5NzN1WWQ3OWk1TzZP'


}

jsondata = {
	'test':'true',
	"language": "es",
	"command": "SUBMIT_TRANSACTION",
	"merchant": {
		"apiLogin": "d7AAkx18XO86E00",
		"apiKey": "85Ne9Eo4r6C3P973uYd79i5O6O"
	}
}


# datos de produccion
# url_produccion_consultas = 'https://api.payulatam.com/reports-api/4.0/service.cgi'
# url_produccion_pagos = 'https://api.payulatam.com/reports-api/4.0/service.cgi'
# merchantid
# APIlogin
# APIKey
# accountId
# headers

# class RealizarPago():


class Plan:

	def Crear():
		data = {
				"accountId": Plan.accountId,
				"planCode": Plan.planCode,
				"description": Plan.description,
				"interval": Plan.interval,
				"intervalCount": Plan.intervalCount,
				"maxPaymentsAllowed": Plan.maxPaymentsAllowed,
				"paymentAttemptsDelay": Plan.paymentAttemptsDelay,
				"additionalValues": [
				{
				"name": "PLAN_VALUE",
				"value": "20000",
				"currency": "COP"
				},
				{
				"name": "PLAN_TAX",
				"value": "3193",
				"currency": "COP"
				},
				{
				"name": "PLAN_TAX_RETURN_BASE",
				"value": "16806",
				"currency": "COP"
				}
				]
		}

		requests.post(url+'plans',headers=headers,data=json.dumps(data))
		return

	def Actualizar():

		requests.put(url+'plans/'+planCode,headers=headers,data=json.dumps(data))
		return

	def Consultar():

		requests.get(url+'plans'+planCode,headers=headers,data=json.dumps(data))
		return

	def Eliminar():
		requests.delete(url+'plans'+planCode,headers=headers,data=json.dumps(data))
		return

class Customers:

	def Post():
		data = {"fullName": fullName, "email": email}
		payu_response = requests.post(url+'customers',headers=headers,data=json.dumps(data))
		return payu_response.text

	def Put():
		data = {"fullName": fullName, "email": email}
		requests.put(url+'customers/'+customerId,headers=headers,data=json.dumps(data))
		return payu_response.text

	def Get():
		requests.get(url+'customers/'+customerId,headers=headers)
		return payu_response.text

	def Delete():
		requests.delete(url+'customers/'+customerId,headers=headers)
		return payu_response.text

class Tarjeta:

	def Post():
		data ={
				"name": name,
				"document": document,
				"number": number,
				"expMonth": expMonth,
				"expYear": expYear,
				"type": type,
				"address": {
					"line1": "Address Name",
					"line2": "17 25",
					"line3": "Of 301",
					"postalCode": "00000",
					"city": "City Name",
					"state": "State Name",
					"country": "CO",
					"phone": "300300300"
				}
		}
		payu_response = requests.post(url+'customers/'+customerId+'/creditCards',headers=headers,data=json.dumps(data))
		return payu_response.text

	def Put():
		data = {
				"expMonth": "12",
				"expYear": "2016",
				"name": "Sample user name",
				"document": "65858645",
				"address": {
					"line1": "Sample Address",
					"line2": "Cll 93 B",
					"line3": "Ofic. 301",
					"postalCode": "00000",
					"city": "city",
					"country": "CO",
					"state": "state",
					"phone": "2266758"
				}
		}
		requests.put(url+'creditCards/'+creditCardId,headers=headers,data=json.dumps(data))
		return payu_response.text

	def Get():
		requests.get(url+'creditCards/'+creditCardId,headers=headers)
		return payu_response.text

	def Delete():
		requests.delete(url+'customers/'+customerId+'/creditCards/'+creditCardId,headers=headers)
		return payu_response.text

class Suscripcion:

	def Post(self):
		data ={
				"quantity": "1",
				"installments": "1",
				"immediatePayment": 'true',
				"extra1": "Extra 1",
				"extra2": "Extra 2",
				"customer": {
					"fullName": "Pedro Perez",
					"email": "pperez@payulatam.com",
					"creditCards": [{
						"name": "Pedro Perez",
						"document": "101010123",
						"number": "4242424242424242",
						"expMonth": "01",
						"expYear": "2018",
						"type": "VISA",
						"address": {
							"line1": "Address Name",
							"line2": "17 25",
							"line3": "Of 301",
							"postalCode": "00000",
							"city": "City Name",
							"state": "State Name",
							"country": "CO",
							"phone": "300300300"
						}
					}]
				},
				"plan": {
					"planCode": "sample-plan-code-001",
				} ,
				"deliveryAddress": {
					"line1": "Address Name",
					"line2": "17 25",
					"line3": "Of 301",
					"postalCode": "00000",
					"city": "City Name",
					"state": "State Name",
					"country": "CO",
					"phone": "300300300"
				},
				"recurringBillItems":{
					"description": "Cargo extra de prueba",
					"additionalValues": [{
						"name": "ITEM_VALUE",
						"value": "20000",
						"currency": "COP"
					},
					{
						"name": "ITEM_TAX",
						"value": "3193",
						"currency": "COP"
					},
					{
						"name": "ITEM_TAX_RETURN_BASE",
						"value": "16806",
						"currency": "COP"
					}
					]
				}
		}
		payu_response = requests.post(url+'subscriptions/',headers=headers,data=json.dumps(data))
		return payu_response.text

	def Put():
		# data =
		requests.put(url+'subscriptions/'+subscriptionId,headers=headers,data=json.dumps(data))
		return payu_response.text

	def Get():
		requests.get(url+'subscriptions/'+subscriptionId,headers=headers)
		return payu_response.text

	def Delete():
		requests.delete(url+'subscriptions/'+subscriptionId,headers=headers)
		return payu_response.text

class Cargos:

	def Post():
		data ={
			"description": "Cargo extra de prueba",
			"additionalValues": [
			{
			"name": "ITEM_VALUE",
			"value": "20000",
			"currency": "COP"
			},
			{
			"name": "ITEM_TAX",
			"value": "3193",
			"currency": "COP"
			},
			{
			"name": "ITEM_TAX_RETURN_BASE",
			"value": "16806",
			"currency": "COP"
			}
			]
			}
		payu_response = requests.post(url+'subscriptions/'+subscriptionId+'recurringBillItems/',headers=headers,data=json.dumps(data))
		return payu_response.text

	def Put():
		data ={
				"description": "Cargo extra de prueba",
				"additionalValues": [
				{
				"name": "ITEM_VALUE",
				"value": "20000",
				"currency": "COP"
				},
				{
				"name": "ITEM_TAX",
				"value": "3193",
				"currency": "COP"
				},
				{
				"name": "ITEM_TAX_RETURN_BASE",
				"value": "16806",
				"currency": "COP"
				}
				]
				}
		requests.put(url+'subscriptions/'+recurringBillItems,headers=headers,data=json.dumps(data))
		return payu_response.text

	def Get():
		requests.get(url+'subscriptions/'+recurringBillItems,headers=headers)
		return payu_response.text

	def Delete():
		requests.delete(url+'subscriptions/'+recurringBillItems,headers=headers)
		return payu_response.text

class Facturas:

	def Get():
		requests.get(url+'recurringBill?customerId='+customerId,headers=headers)
		return payu_response.text
