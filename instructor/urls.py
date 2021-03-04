from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.instructor_registration, name='register'),
    path('login/', views.instructor_login, name='login'),
    path('logout/', views.instructor_logout, name='logout'),
    path('dashboard/', views.instructor_dashboard, name='dashboard'),
    path('settings/', views.instructor_settings, name='settings'),
    path('create-game/', views.create_game, name='create-game'),
]