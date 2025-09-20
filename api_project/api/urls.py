
from django.urls import path
from .views import BookListView
urlpatterns = [
    path("Book/", BookListView.as_view(), name="Book")
]