
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home.as_view(), name= "home"),
    path("list_books/", views.list_books, name= "list_books"),
    path("library_detail/", views.library_detail.as_view(), name="library_detail"),
    path("login/", views.login.as_view(template_name = "login.html"), name="login"),
    path("logout/", views.logout.as_view(template_name = "logout.html"), name="logout"),
    path("register/", views.register.as_view(template_name = "register.html"), name="register"),
]