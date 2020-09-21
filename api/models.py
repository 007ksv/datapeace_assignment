from django.db import models

# This is the model that we are going to user for this project

class CustomUser(models.Model):

	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	company_name = models.CharField(max_length=80)
	age = models.PositiveIntegerField()
	city = models.CharField(max_length=40)
	state = models.CharField(max_length=40)
	zip = models.PositiveIntegerField()			
	email = models.EmailField(max_length=100)
	web = models.URLField(max_length=255)


	# Defining string representaion of our model

	def __str__(self):
		return self.email


