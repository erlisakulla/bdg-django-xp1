from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def game_registration(request):
	return render(request, 'student/student-game-registration.html')

def enter_game(request):
	return render(request, 'student/student-enter-game.html')

def create_game(request):
	return HttpResponse('Create Game')