from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import SoolGame,Recipes,Users,Tip
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def boardList(request,type):
	if(type=='0'):		#SoolGame
		list = SoolGame.objects.order_by('TITLE')
	elif(type=='1'):	#Recipes
		list = Recipes.objects.order_by('TITLE')
	else:				#Tip
		list = Tip.objects.order_by('TITLE')

	records = []
	for tmp in list:
		title = tmp.TITLE
		like = tmp.LIKE
		context = tmp.CONTEXT
		uploader = tmp.UPLOADER
		photo = tmp.PHOTO
		record = {
			'title':title,
			'like':like,
			'context':context,
			'uploader':uploader,
			'photo':photo,
		}
		records.append(record)

	return HttpResponse(records,content_type="application/json")

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