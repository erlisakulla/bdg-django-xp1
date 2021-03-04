<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.instructor_registration, name='register'),
    path('login/', views.instructor_login, name='login'),
    path('logout/', views.instructor_logout, name='logout'),
    path('dashboard/', views.instructor_dashboard, name='dashboard'),
    path('settings/', views.instructor_settings, name='settings'),
    path('create-game/', views.create_game, name='create-game'),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.instructor_registration),
    path('login/', views.instructor_login),
    path('instructor/', views.instructor_dashboard)
>>>>>>> ce29bf3716dd0ce95bd0600ec0cc41dbd2acf737
]