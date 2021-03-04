from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import InstructorUser

from django import forms

class InstructorRegistrationForm(UserCreationForm):
	error_css_class = "error"
	class Meta:
		model = InstructorUser
		fields = ['full_name', 'email', 'password1', 'password2']