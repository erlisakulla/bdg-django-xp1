from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.instructor_registration),
    path('login/', views.instructor_login),
    path('instructor/', views.instructor_dashboard)
]