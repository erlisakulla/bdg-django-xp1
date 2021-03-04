from django.shortcuts import render
from django.http import HttpResponse
from student.models import *
from .models import *
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

#first needs to be changed, the idea is to prepend id to instructor, but i don't know ids of instructors
def instructor_dashboard(request):
	instructor = Instructor.objects.first()
	# instructor = Instructor.objects.get(id=pk)
	students = Student.objects.all()
	# quite risky to have fks as full name
	students_for_instructor = Student.objects.filter(instructor_name=instructor.id)
	
	
	context = {'students': students_for_instructor, 'instructor': instructor}
	return render(request, 'instructor/dashboard.html', context)