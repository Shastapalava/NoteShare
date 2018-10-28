from django.db import models

class ordUser(models.Model):
	firstName = models.CharField()
	lastName = models.CharField()
	email = models.EmailField()
	password = models.CharField() #do not leave password as is. Handle with hashing later on

class Note(models.Model):
	creationDate = models.DateTimeField()
	
