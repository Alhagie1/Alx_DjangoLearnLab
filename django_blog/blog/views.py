from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib import messages

# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("blog:profile")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")
    

    return render(request, "login.html")


# Logout View
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect("login")
    

    return render(request, "logout.html")

# Custom Registration Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

# Register View
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")
            login(request, user)  # Auto login after registration
            return redirect("blog:profile")
        else:
            return render(request, "register.html", {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, "register.html", {"form": form})

# Profile View
@login_required(login_url="login")
def profile_view(request):
    return render(request, "profile.html")