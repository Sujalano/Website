from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile
from django.contrib.auth.models import User
from .backends import EmailBackend
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        data = request.POST
        uname = data.get('username')

        # 1. Check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, f"The username '{uname}' is already taken. Please choose another.")
            return render(request, "dashboard/register.html")

        try:
            # 2. Create the User
            user = User.objects.create_user(
                username=uname,
                email=data.get('email'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name')
            )
            
            # 3. Create the Profile
            Profile.objects.create(user=user, user_type="SCHOOL")
            
            messages.success(request, "Account created successfully!")
            return redirect('login')
            
        except Exception as e:
            messages.error(request, "An error occurred during registration.")
            return render(request, "dashboard/register.html")

    return render(request, "dashboard/register.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # Added request as first arg
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, "dashboard/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
