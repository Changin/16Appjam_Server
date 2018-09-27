from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import SoolGame,Recipes,Tip
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

@csrf_exempt
def signup(request):	#회원가입
	mail = request.POST['email']	#이메일을 로그인 아이디로 사용
	try:
		user_id = User.objects.get(email=mail) #아이디 중복 확인

		register_data = {
			'status':'0'	#id already taken!
		}
		return JsonResponse(register_data) #회원가입 실패

	except:
		pw = request.POST['pw']
		name = request.POST['name']
		new_user = User.objects.create_user(email=mail,nickname=name,password=pw)
		#user 생성
		new_user.save()

		register_data = {
			'status':'1'
		}
		return JsonResponse(register_data)