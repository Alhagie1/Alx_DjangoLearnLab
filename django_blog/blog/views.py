# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # ← ADD THIS!
from django import forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpRequest
from .models import Post
from .forms import PostForm  

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
            login(request, user)  
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

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "profile.html"  
    fields = ["title", "content"]
    success_url = reverse_lazy('blog:home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = "post_form.html"  
    fields = ["title", "content"]
    success_url = reverse_lazy('blog:home')
    raise_exception = False
    redirect_field_name = None
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostListView(generic.ListView):
    model = Post
    template_name = "post_list.html"  
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 10

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"  
    context_object_name = 'post'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = "post_delete.html"  
    success_url = reverse_lazy('blog:home')
    raise_exception = False
    redirect_field_name = None

    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author