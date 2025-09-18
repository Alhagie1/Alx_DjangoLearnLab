
from asyncio import all_tasks
from .models import Book, Librarian, Library

book = Book.objects.filter(author = "NjolTech")

library = Library.objects.get(library_name="Public Libary")
books = Library.books.all()

try:
   librarian = Librarian.objects.get(librarian_name = "John Rix")
except Librarian.DoesNotExist:
   print("model does not exist")
except Librarian.MultipleObjectsReturned:
   print("Many objects are return.")