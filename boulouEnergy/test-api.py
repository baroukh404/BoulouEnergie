import requests
import time

endpoint = "http://localhost:8000/SmartPlug/checkStatus"
deviceId = "bfbbe603f37b831375vgzq"
actual_power = 0
threshold = 0
data = {
	'deviceId': deviceId,
	'actual_power': 'actual_power',
	'threshold': 'threshold',
	'message': 'vous avez atteint la puissance maximun'
}

# def overload(actual_power, threshold):
# 	actual_power = 30
# {"switch":true,"actual_current":0.365,"actual_voltage":221.2,"actual_power":46.1}


def sendSMS():
	endpoint = "http://localhost:8000/SmartPlug/send-sms"
	data['message'] = 'vous avez atteint la puissance maxumim autoriser'
	client = requests.post(endpoint, data)

while True:
	# device status
	checkStatus = requests.get("http://localhost:8000/SmartPlug/checkStatus", json=data)
	checkStatus = checkStatus.json()
	devStatus = checkStatus['switch']
	
	if devStatus:
		pass			
	else:
		client = requests.post("http://localhost:8000/SmartPlug/switch-ON", data)
		print("normal working")
		print(client.json())

	# actual_power
	endpoint = "http://localhost:8000/SmartPlug/checkStatus"
	client = requests.get(endpoint, json=data)
	actual_power = client.json()['actual_power']
	threshold = 40     # user defined
	data['actual_power'] = actual_power
	data['threshold'] = threshold
	
	if threshold < actual_power:
		sendSMS()
		endpoint = "http://localhost:8000/SmartPlug/switch-OFF"
		client = requests.post(endpoint, data)
		client = requests.post(endpoint, json=data)
		# print(client.json())
		
		# wait 5 min to turn on smart-plug
		time.sleep(300)
		# break

	# if client.json() == True:
	# 	print("overload")
	# 	print("alert sent, the smart-plug is powering down")
	time.sleep(30)