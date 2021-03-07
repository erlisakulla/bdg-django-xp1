from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import *
from .models import *
from game.models import *

from .forms import InstructorRegistrationForm
from game.forms import GameCreationForm
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

	students_for_instructor = Student.objects.filter(instructor_name=request.user.id)
	
	context = {'students':students_for_instructor, 'myFilter':myFilter}

	return render(request, 'instructor/dashboard.html', context)

@login_required(login_url='login')
def instructor_settings(request):
	context = {}
	return render(request, 'instructor/settings.html', context)

@login_required(login_url='login')
def create_game(request):
	form_name = "Create Game"

	form = GameCreationForm()
	if request.method == 'POST':
		form = GameCreationForm(request.POST)

		if form.is_valid():
			#set foreign key of instructor	
			nf = form.save(commit=False)
			nf.instructor = InstructorUser.objects.get(id=request.user.id)
			nf.save()
		
			return redirect('games-list')
			#redirect to view games
		
	context = {'form':form, 'form_name':form_name}
	return render(request, 'instructor/create-game.html', context)

@login_required(login_url='login')
def games_list(request): # (request, pk)
	#games = Game.objects.all()
	#filtered to instructor
	games = Game.objects.filter(instructor=request.user.id)
	
	context = {'games':games}
	return render(request, 'instructor/games-list.html', context)

@login_required(login_url='login')
def update_game(request, pk):
	form_name = "Update Game"

	game = Game.objects.get(game_id=pk)
	form = GameCreationForm(instance=game)

	if request.method == 'POST':
		form = GameCreationForm(request.POST, instance=game)

		if form.is_valid():
			form.save()
			return redirect('games-list')

	context = {'form_name':form_name, 'form':form}
	return render(request, 'instructor/create-game.html', context)

@login_required(login_url='login')
def delete_game(request, pk):
	form_name = "Delete Game"

	game = Game.objects.get(game_id=pk)

	if request.method == 'POST':
		game.delete()
		return redirect('games-list')

	context = {'form_name':form_name, 'game':game}
	return render(request, 'instructor/delete-game.html', context)