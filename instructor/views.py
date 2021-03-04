<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import *

from .forms import InstructorRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .filters import StudentFilter

from django.contrib.auth.decorators import login_required

# Create your views here.

def instructor_registration(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = InstructorRegistrationForm()
		if request.method == 'POST':
			form = InstructorRegistrationForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('full_name')
				messages.success(request, 'Account created successfully for ' + user)
				return redirect('login')

		context = {'form':form}
		return render(request, 'instructor/instructor-registration.html', context)

def instructor_login(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'instructor/instructor-login.html', context)

def instructor_logout(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def instructor_dashboard(request):
	students = Student.objects.all()

	myFilter = StudentFilter(request.GET, queryset=students)
	students = myFilter.qs

	context = {'students':students, 'myFilter':myFilter}

	return render(request, 'instructor/dashboard.html', context)

@login_required(login_url='login')
def instructor_settings(request):
	context = {}
	return render(request, 'instructor/settings.html', context)

# @login_required(login_url='login')
def create_game(request):
	context = {}
	return render(request, 'instructor/create-game.html', context)
=======
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
>>>>>>> ce29bf3716dd0ce95bd0600ec0cc41dbd2acf737
