from django.forms import ModelForm
from .models import Game

from django import forms

class GameCreationForm(forms.ModelForm):
	class Meta:
		model = Game
		fields = '__all__'
		exclude = ('instructor',)