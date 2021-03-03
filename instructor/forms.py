from django.forms import ModelForm
from .models import Instructor

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InstructorRegistrationForm(forms.ModelForm):
	class Meta:
		model = Instructor
		fields = ['full_name', 'email', 'password']