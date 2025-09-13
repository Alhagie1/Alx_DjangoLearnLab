
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home.as_view, name= "home"),
    path("list_books/", views.list_books.as_view(), name= "list_books"),
    path("library_detail/", views.library_detail.as_view(), name="library_detail"),
    path("login/", views.login.as_view(), name="login"),
    path("logout/", views.logout.as_view(), name="logout"),
    path("register/", views.register.as_view(), name="regiter"),
]