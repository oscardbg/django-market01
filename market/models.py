from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	description = models.CharField(max_length=1025)
	image_url = models.CharField(max_length=512)
	owner = models.ForeignKey(User, default=None, blank=True, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name