from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  #to add message functionality to the project.
from .forms import SetupForm

# Create your views here.
def index(request):
    return render(request, "authenticate/home.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in!'))
            return redirect('home') 
        else:
            messages.success(request, ('Error Logging in - Please Try Again....'))

            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out...'))
    return redirect('home')

def register_user(request):
        if request.method == "POST":
            form = SetupForm(request.POST)  #creation of new user
            if form.is_valid:   #if the form is valid
                try:
                    form.save()     #save the form
                except:
                    messages.success(request, ('Somehting went wrong'))
                    return redirect('register')
                    
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username = username, password = password)
                login(request, user)
                messages.success(request, ('You have Registered now!'))

        else:
            form = SetupForm()

        context = {"form":form}
        return render(request, "authenticate/register.html", context)
    