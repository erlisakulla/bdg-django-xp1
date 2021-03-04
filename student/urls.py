<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('game-registration/', views.game_registration),
    path('enter-game/', views.enter_game),
    path('create-game/', views.create_game),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('game-registration/', views.game_registration),
    path('enter-game/', views.enter_game),
    path('create-game/', views.create_game),
>>>>>>> ce29bf3716dd0ce95bd0600ec0cc41dbd2acf737
]