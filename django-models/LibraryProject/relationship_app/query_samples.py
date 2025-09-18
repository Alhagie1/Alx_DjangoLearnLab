
from asyncio import all_tasks
from .models import Book, Librarian, Library

book = Book.objects.filter(author = "NjolTech")

Library.objects.get(name="library_name")
books = Library.books.all()

try:
   Librarian.objects.get(name="librarian_name")
except Librarian.DoesNotExist:
   print("model does not exist")
except Librarian.MultipleObjectsReturned:
   print("Many objects are return.")