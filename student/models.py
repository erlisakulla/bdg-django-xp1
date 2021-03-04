from django.db import models

# Create your models here.

class Student(models.Model):
	full_name = models.CharField(max_length=50)
	# instructor_name = models.CharField(max_length=50)
	instructor_name = models.ForeignKey('instructor.Instructor', null=True, on_delete=models.SET_NULL)
	email = models.EmailField(max_length=50)
	time_registered = models.DateField(max_length=50, null=True)
	
	#string of game ids separated by , 
	assigned_games = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.full_name