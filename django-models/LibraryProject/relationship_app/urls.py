
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetails
urlpatterns = [
    path("", views.home.as_view(), name= "home"),
    path("list_books/", views.list_books, name= "list_books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("login/",LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/",LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/",views.register.as_view(template_name = "register.html"), name="register"),
    path("admin_view/", views.admin_view.as_view(template_name="admin_view.html"), name="admin view"),
    path("librarian_view/", views.librarian_view.as_view(template_name="librarian_view.htm"), name="librarian view"),
    path("member_view/", views.member_view.as_view(template_name="member_view.html"), name="member view"),
    path("can_add_book/", views.can_edit_book.as_view(), name=" can add book"),
    path("can_change_book/", views.can_change_book.as_view(),name="can change book"),
    path("can_delete_book/", views.can_edit_book.as_view(), name="can delete book"),
]