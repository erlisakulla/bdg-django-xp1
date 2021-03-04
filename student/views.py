<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

from .forms import StudentGameRegistrationForm


# Create your views here.
def game_registration(request):
	form = StudentGameRegistrationForm()

	if request.method == 'POST':
		form = StudentGameRegistrationForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'student/student-game-registration.html', context)

def enter_game(request):
	return render(request, 'student/student-enter-game.html')

def create_game(request):
=======
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def game_registration(request):
	return render(request, 'student/student-game-registration.html')

def enter_game(request):
	return render(request, 'student/student-enter-game.html')

def create_game(request):
>>>>>>> ce29bf3716dd0ce95bd0600ec0cc41dbd2acf737
	return HttpResponse('Create Game')