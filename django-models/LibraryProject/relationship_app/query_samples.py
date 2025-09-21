
from asyncio import all_tasks
from .models import Book, Librarian, Library

# Query samples as strings in lists
author_queries= [
    "Author.objects.get(name=author_name)",
    "objects.filter(author=author)"
]

library_queries = [
    "Library.objects.get(name=library_name)", 
   "books.all()"
]

librarian_queries = [
    "Librarian.objects.get(name='John')"
]

try:
   Librarian.objects.get(name="Josh")
except Librarian.DoesNotExist:
   print("model does not exist")
except Librarian.MultipleObjectsReturned:
   print("Many objects are return.")