from django.forms import ModelForm
from .models import Student

from django import forms

class StudentGameRegistrationForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['full_name', 'instructor_name', 'email']