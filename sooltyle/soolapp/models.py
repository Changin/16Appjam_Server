from django.db import models
from django.utils import timezone

class SoolGame(models.Model):
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()

	def __str__(self):
		return self.title


class Recipes(models.Model):
	TITLE = models.CharField(max_length=40)
	LIKE = models.IntegerField()
	CONTEXT = models.TextField()
	UPLOADER = models.CharField(max_length=40)
	PHOTO = models.TextField()

	def __str__(self):
		return self.title


class Users(models.Model):
	USER_ID = models.CharField(max_length=40)
	USER_PW = models.CharField(max_length=20)
	USER_NAME = models.CharField(max_length=40)

	def __str__(self):
		return self.title