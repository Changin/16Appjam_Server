from django.shortcuts import render, get_object_or_404
#from django.utils import simplejson
import json
from django.http import HttpResponse
from .models import SoolGame,Recipes,Users

def register(request,id,pw,name):
	#register
	try:
		user_id = Users.objects.get(USER_ID=id)

	except ObjectDoesNotExist:
		return 1

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

	data = simplejson.dumps(some_data_to_dump)
	return HttpResponse(data,content_type='application/json')