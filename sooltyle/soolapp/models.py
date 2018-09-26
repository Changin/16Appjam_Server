from django.db import models
from django.utils import timezone

class Tip(models.Model):	#팁 게시판
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()

class SoolGame(models.Model):#술게임 게시판
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()

class Recipes(models.Model):#레시피 게시판
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()