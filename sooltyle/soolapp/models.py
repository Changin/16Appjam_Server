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