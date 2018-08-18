from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import SoolGame,Recipes,Users

def register(request,id,pw,name):
	#register
	try:
		user_id = Users.objects.get(USER_ID=id)

	except ObjectDoesNotExist:
		

def login(request,id,pw):
	#login
	try:
		user_id = Users.objects.get(USER_ID=id)
		user_pw = Users.objects.get(USER_PW=pw)

		login_data = {
			'status':'1',
		}

	except ObjectDoesNotExist:
		login_data = {
			'status':'0',
		}

	return JsonResponse(login_data)