
from django.urls import path
from .views import BookList
urlpatterns = [
    path("Book/", BookList.as_view(), name="Book")
]