# gym/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import built-in login view

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration page
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login page using Django's built-in view
]
