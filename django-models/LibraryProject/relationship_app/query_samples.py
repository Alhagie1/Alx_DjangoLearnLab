
from asyncio import all_tasks
from .models import Book, Librarian, Library

book = Book.objects.filter(author = "NjolTech")

books = Library.objects.get(name= "library_name")
books.all()

try:
   librarian = Librarian.objects.get(name = "John Rix")
except Librarian.DoesNotExist:
   print("model does not exist")
except Librarian.MultipleObjectsReturned:
   print("Many objects are return.")