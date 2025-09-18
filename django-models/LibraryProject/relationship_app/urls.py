
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path("", views.home.as_view(), name= "home"),
    path("list_books/", views.list_books, name= "list_books"),
    path("library_detail/", views.LibraryDetails.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name = ""), name="login"),
    path("logout/", LogoutView.as_view(template_name = ""), name="logout"),
    path("register/", views.register.as_view(template_name = "register.html"), name="register"),
]