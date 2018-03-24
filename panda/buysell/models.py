from django.db import models

class Account(models.Model):
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	username = models.CharField(max_length=200, primary_key=True)
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	datecreated = models.DateTimeField('Date Created')

	def __str__(self):
		return self.username