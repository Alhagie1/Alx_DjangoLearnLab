
from django.urls import path
from django.contrib.auth import views
from .views import  login_view, logout_view,profile_view, register_view

urlpatterns = [
    path("login/",login_view, name="login"),
    path("logout/", logout_view,name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile")
]