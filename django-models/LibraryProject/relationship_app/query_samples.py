
from asyncio import all_tasks
from .models import Book, Librarian, Library

book = Book.objects.filter(author = "NjolTech")

library = Library.objects.get(name="Public Libary")
books = Library.books.all()

try:
   librarian = Librarian.objects.get(name = "John Rix")
except Librarian.DoesNotExist:
   print("model does not exist")
except Librarian.MultipleObjectsReturned:
   print("Many objects are return.")