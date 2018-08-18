from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import SoolGame,Recipes,Users
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def boardList(request,type):
	if(type=='0'):		#SoolGame
		list = SoolGame.objects.order_by('-pub_date')
	elif(type=='1'):	#Recipes
		list = Recipes.objects.order_by('-pub_date')
	else:
		list = Users.objects.order_by('-pub_date')

	return JsonResponse(list)

@csrf_exempt
def register(request,id,pw,name):	#register
	#register
	try:
		user_id = Users.objects.get(USER_ID=id)
		register_data = {
			'status':'0'	#id already taken!
		}
		return JsonResponse(register_data)

	except:
		user = Users(USER_ID=id,USER_PW=pw,USER_NAME=name)
		user.save()
		register_data = {
			'status':'1'
		}
		return JsonResponse(register_data)

@csrf_exempt
def login(request,id,pw):			#login
	#login
	try:
		user_id = Users.objects.get(USER_ID=id)
		user_pw = Users.objects.get(USER_PW=pw)

		login_data = {
			'status':'1',
		}

	except:
		login_data = {
			'status':'0',
		}

	return JsonResponse(login_data)