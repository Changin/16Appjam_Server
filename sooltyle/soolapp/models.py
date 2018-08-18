from django.db import models
from django.utils import timezone

class Tip(models.Model):
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()

class SoolGame(models.Model):
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()


class Recipes(models.Model):
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()


class Users(models.Model):
	USER_ID = models.CharField(max_length=40)
	USER_PW = models.CharField(max_length=20)
	USER_NAME = models.CharField(max_length=40)