# gym/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    # Add extra fields to the form
    email = forms.EmailField()  # Add email field
    first_name = forms.CharField(max_length=100)  # Add first name field
    
    class Meta:
        model = User  # Link to Django's User model
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        # Include the username, email, password1, and password2 fields
