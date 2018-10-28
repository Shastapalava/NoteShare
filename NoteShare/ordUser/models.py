from django.db import models

class ordUser(models.Model):
	firstName = models.CharField(max_length = 100)
	lastName = models.CharField(max_length = 100)
	email = models.EmailField(max_length = 100)
	password = models.CharField(max_length = 100) #do not leave password as is. Handle with hashing later on

class Note(models.Model):
	creationDate = models.DateTimeField()
	
