import django_filters
from django.forms.widgets import TextInput
from django import forms


from student.models import *

class StudentFilter(django_filters.FilterSet):
	full_name = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Search students . .'}))
	class Meta:
		model = Student
		fields = ['full_name']