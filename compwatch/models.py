from django.db import models

# Create your models here.
class Page(models.Model):
	name = models.CharField(max_length="20",primary_key=True)
	content = models.TextField(blank=True)

class Data(models.Model):
	context = models.CharField(max_length="20")
	name = models.CharField(max_length="20")
	url = models.CharField(max_length="20")
	country = models.CharField(max_length="20")
	active_since = models.DateTimeField()
	location = models.CharField(max_length="20")
	totalmembers = models.CharField(max_length="20",blank="True",null="True")
	facebook = models.CharField(max_length="20",blank="True",null="True")
	twitter = models.CharField(max_length="20",blank="True",null="True")
	traffic_world = models.CharField(max_length="20",blank="True",null="True")
	traffic_country = models.CharField(max_length="20",blank="True",null="True")


	
