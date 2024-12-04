# gym/views.py
from django.shortcuts import render,redirect
from .models import Member
from .forms import RegisterForm
def member_list(request):
    # Fetch all members from the database
    members = Member.objects.all()
    # Render the 'member_list.html' template, passing the members as context
    return render(request, 'gym/member_list.html', {'members': members})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():  # Check if form is valid
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()  # Create an empty form for GET request

    return render(request, 'gym/register.html', {'form': form})