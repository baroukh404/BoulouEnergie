from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.conf import settings
import requests
import json


email = "rrabeandriamarozoky@gmail.com"
developerId = "-NlmAu0LM0-NaqRuWosx"
deviceId = "bfbbe603f37b831375vgzq"
endpoint = "https://us-central1-boulou-functions-for-devs.cloudfunctions.net/"




# application home-page
class Home(APIView):
	def get(self, request):
		return render(request, 'home.template.html')

# login home-page
class Login(APIView):
    def get(self, request):
        username = "IHOBIMANARIVO RakotobeSalimo"
        return render(request, 'login.template.html', context={'username': username}, status=200)

    def post(self, request):
        return Response({'token': 'token.key'}, status=status.HTTP_200_OK)

# smart-plug list page
class Inventaire(APIView):
	def get(self, request):
		return Response({'response': 'Inventaire Page ...'}, status=status.HTTP_200_OK)

# control-page
class Control(APIView):
	def get(self, request):
		return Response({'response': 'Control Page ...'}, status=status.HTTP_200_OK)

# for user management: admin access only
class UserManagement(APIView):
	def get(self, request):
		return Response({'response': 'UserManagement Page ...'}, status=status.HTTP_200_OK)

# for user settings
class UserSettings(APIView):
	def get(self, request):
		return Response({'response': 'UserSettings Page ...'}, status=status.HTTP_200_OK)



# switch on the smart_plug
class SwitchOn(APIView):
	def post(self, request):
		deviceId = request.data.get('deviceId')
		url = f"{endpoint}"+"boulou_switch_device"
		body = {
			"developerId": f"{developerId}",
			"email": f"{email}",
			"deviceId": f"{deviceId}",
			"switch_status": "ON"
		}
		client = requests.post(url, json=body)
		return Response({'status': 'switched-ON', 'deviceId': deviceId}, status=status.HTTP_200_OK)

# switch off the smart-plug
class SwitchOff(APIView):
	def post(self, request):
		deviceId = request.data.get('deviceId')
		url = f"{endpoint}"+"boulou_switch_device"
		body = {
			"developerId": f"{developerId}",
			"email": f"{email}",
			"deviceId": f"{deviceId}",
			"switch_status": "OFF"
		}
		client = requests.post(url, json=body)
		return Response({'status': 'switched-OFF', 'deviceId': deviceId}, status=status.HTTP_200_OK)

# get the status of the smart-plug ['on', 'off']
class CheckStatus(APIView):
	def get(self, request):
		deviceId = request.data.get('deviceId')
		url = f"{endpoint}"+f"boulou_check_deviceStatus?developerId={developerId}&email={email}&deviceId={deviceId}"
		client = requests.get(url)
		devStatus = client.json()
		devStatus = devStatus['result']['status']
		return Response(devStatus, status=status.HTTP_200_OK)

# get all the statistics of the smart-plug
class GetStatistics(APIView):
	def get(self, request):
		year = 'year'
		year_value = 2023
		url = f"{endpoint}"+f"boulou_get_deviceStatistics?developerId={developerId}&email={email}&deviceId={deviceId}&period_type={year}&period_value={year_value}"
		client = requests.get(url)
		response = client.json()
		return Response(response, status.status.HTTP_200_OK)

# custom max power: maximum power=4000w
class CustomPower(APIView):
	def post(self, request):
		power = request.data.get('cutom_power')
		return Response({'message': 'custom power set'}, status=status.HTTP_200_OK)

# timer funtion
class TimerCountDown(APIView):
	def post(self, request):
		return Response({'msg': 'TimerCountDown'}, status=status.HTTP_200_OK)

# timer shchedule
class TimerSchedule(APIView):
	def post(self, request):
		return Response({'msg': 'TimerSchedule'}, status=status.HTTP_200_OK)

# overload smart-plug
# {
# 	"success": True,
# 	"result": {
# 		"id": "bfbbe603f37b831375vgzq",
# 		"name": "BAROUKH404",
# 		"online": true,
# 		"status": {
# 			"switch": true, 
# 			"actual_current": 0.432, 
# 			"actual_voltage": 228.9, 
# 			"actual_power": 56.2 
# 			}
# 		}
# } .json()['result']['status']


# OVERLOAD
# def powerDownOverload(threshold, actual_power):
# 	if threshold < actual_power:
# 		deviceId = request.data.get('deviceId')
# 		url = f"{endpoint}"+"boulou_switch_device"
# 		body = {
# 			"developerId": f"{developerId}",
# 			"email": f"{email}",
# 			"deviceId": f"{deviceId}",
# 			"switch_status": "OFF"
# 		}
# 		client = requests.post(url, json=body)
# 		return Response({'status': 'switched-OFF', 'deviceId': deviceId}, status=status.HTTP_200_OK)

class OverLoad(APIView):
	def post(self, request):
		deviceId = request.data.get('deviceId')
		actual_power = request.data.get('actual_power')
		threshold = request.data.get('threshold')
		# checking
		if threshold < actual_power:
			# url = f"{endpoint}"+"boulou_switch_device"
			# body = {
			# 	"developerId": f"{developerId}",
			# 	"email": f"{email}",
			# 	"deviceId": f"{deviceId}",
			# 	"switch_status": "OFF"
			# }
			# client = requests.post(url, json=body)
			# send_sms()
			return Response({'status': True}, status=status.HTTP_200_OK)

		else:
			return Response({'status': False}, status=status.HTTP_200_OK)


class SendSMS(APIView):
	def post(self, request):
		return Response({'message': 'sms_sent'})