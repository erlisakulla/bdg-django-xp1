from django.db import models


# Create your models here.

class Instructor(models.Model):
	full_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=32)

	def __str__(self):
		return self.full_name