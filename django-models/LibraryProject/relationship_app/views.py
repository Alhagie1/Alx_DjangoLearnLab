from django.shortcuts import redirect, render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
def list_books(request):
    """List the details of the book"""
    all_books = Book.objects.all()
    return render (request, "relationship_app/list_books.html",{"all_books": all_books})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
class LibraryDetails(ListView):
    model = Book
    template_name = "relationship_app/library_detail.html"
    context_object_name = "books"
    