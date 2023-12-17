from django.shortcuts import render
from django.http import HttpResponse
import requests


email = "rrabeandriamarozoky@gmail.com"
developerId = "-NlmAu0LM0-NaqRuWosx"
deviceId = "bfbbe603f37b831375vgzq"

def smart_plug(request, switch=""):
	device = SmartPlug(deviceId)
	if switch == 'on':
		device.switchON()
	if switch == 'off':
		device.switchOFF()
	return render(request, 'smart_plug.html')


class SmartPlug:
	def __init__(self, deviceId):
		self.deviceId = deviceId
		self.year = 0
		self.year_value = 0

	def checkStatus(self):
		url = f"https://us-central1-boulou-functions-for-devs.cloudfunctions.net/boulou_check_deviceStatus?developerId={developerId}&email={email}&deviceId={deviceId}"
		client = requests.get(url)
		# response = client.json()
		# return response
		
	def switchON(self):
		url = f"https://us-central1-boulou-functions-for-devs.cloudfunctions.net/boulou_switch_device"
		body = {
			"developerId": f"{developerId}",
			"email": f"{email}",
			"deviceId": f"{deviceId}",
			"switch_status": "ON"
		}
		client = requests.post(url, json=body)
		# response = client.json()
		# return response

	def switchOFF(self):
		url = f"https://us-central1-boulou-functions-for-devs.cloudfunctions.net/boulou_switch_device"
		body = {
			"developerId": f"{developerId}",
			"email": f"{email}",
			"deviceId": f"{deviceId}",
			"switch_status": "OFF"
		}
		client = requests.post(url, json=body)
		# response = client.json()
		# return response

	def getStatistics(self, year, year_value):
		year = year
		year_value = year_value
		url = f"https://us-central1-boulou-functions-for-devs.cloudfunctions.net/boulou_get_deviceStatistics?developerId={developerId}&email={email}&deviceId={deviceId}&period_type={year}&period_value={year_value}"
		client = requests.get(url)
		response = client.json()
		return response
