from django.shortcuts import render
from django.http import HttpResponse
from student.models import *
from django.contrib.auth.forms import UserCreationForm

from .forms import InstructorRegistrationForm

# Create your views here.

def instructor_registration(request):
	form = InstructorRegistrationForm()

	if request.method == 'POST':
		form = InstructorRegistrationForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'instructor/instructor-registration.html', context)

def instructor_login(request):
	return render(request, 'instructor/instructor-login.html')

def instructor_dashboard(request):
	students = Student.objects.all()
	return render(request, 'instructor/dashboard.html', {'students':students})