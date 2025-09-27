from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import permission_required,REDIRECT_FIELD_NAME
from .models import Book
def index(request):
    return render(request, 'booshelf/')

editors = Group.objects.get(name= "Editors")
viewers = Group.objects.get(name="Viewers")
admins = Group.objects.get(name="Admins")

editors_group = Permission.objects.filter(codename__in=[
    ("can_edit"),
    ("can_create"),
   ("can_view") ,
   ("can_add"),
])

viewers_group = Permission.objects.filter(codename=("can_view", ),
)

admins_group = Permission.objects.all()

editors.permissions.set(editors_group)
viewers.permissions.set(viewers_group)
admins.permissions.set(admins_group)

print("group permissions created successfully.")

@permission_required('booshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'booshelf/book_list.html', {'books': books})


@permission_required('booshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle book creation logic here
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(
            title=title,
            author=author,
            created_by=request.user
        )
        messages.success(request, 'Book created successfully!')
        return redirect('book_list')
    return render(request, 'booshelf/create_book.html')

@permission_required('booshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        # Handle book editing logic here
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('book_list')
    return render(request, 'booshelf/edit_book.html', {'book': book})

@permission_required('booshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('book_list')