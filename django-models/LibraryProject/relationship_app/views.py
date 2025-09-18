from django.shortcuts import redirect, render

import relationship_app
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
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

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view - only accessible to Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view - only accessible to Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view - only accessible to Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required(relationship_app.can_add_book)

def add_book(request):
    return render, "realtionship_app/add_book.html"

@permission_required(relationship_app.can_edit_book)

def can_edit_book(request):

    return render, "relationship_app/can_edit_book.html"

@permission_required(relationship_app.can_delete_book)

def delete_book(request):

    return render, "relationship_app/can_delete_book.html"