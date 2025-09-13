
from .models import Book, Librarian

book = Book.objects.filter(author = "NjolTech")

all_books = Book.objects.all()
print(f"The books in the library include: {all_books}")
try:
   librarian = Librarian.objects.get(name = "John Rix")
except Librarian.DoesNotExist:
   print("model does not exist")
except Librarian.MultipleObjectsReturned:
   print("Many objects are return.")