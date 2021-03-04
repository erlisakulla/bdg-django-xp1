<<<<<<< HEAD
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import InstructorUser

from django import forms

class InstructorRegistrationForm(UserCreationForm):
	error_css_class = "error"
	class Meta:
		model = InstructorUser
		fields = ['full_name', 'email', 'password1', 'password2']
=======
from django.forms import ModelForm
from .models import Instructor

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InstructorRegistrationForm(forms.ModelForm):
	class Meta:
		model = Instructor
		fields = ['full_name', 'email', 'password']
>>>>>>> ce29bf3716dd0ce95bd0600ec0cc41dbd2acf737
