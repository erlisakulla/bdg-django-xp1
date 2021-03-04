from django.urls import path
from . import views

urlpatterns = [
    path('game-registration/', views.game_registration),
    path('enter-game/', views.enter_game),
    path('create-game/', views.create_game),
]