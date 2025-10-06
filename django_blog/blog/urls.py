from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view, profile_view, register_view
from .views import (
    PostListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView
)

app_name = 'blog'  # ← IMPORTANT! Add this for namespacing

urlpatterns = [
    # Auth URLs
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    
    # Blog CRUD URLs
    path("", PostListView.as_view(), name="home"), 
    path("post/new/", PostCreateView.as_view(), name="post-create"),  
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"), 
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  
]