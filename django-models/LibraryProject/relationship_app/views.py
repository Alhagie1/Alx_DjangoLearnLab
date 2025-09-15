from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
def list_books(request):
    """List the details of the book"""
    all_books = Book.objects.all()
    return render (request, "list_books.html",{"all_books": all_books})

class LibraryDetails(ListView):
    model = Book
    template_name = "library_details.html"
    context_object_name = "books"
    
    