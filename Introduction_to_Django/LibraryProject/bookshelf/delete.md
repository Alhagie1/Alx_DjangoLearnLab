
Delete 

This is a process of removing a database object 
command:
from bookshelf.models import Book
new_book = Book.object.get(publication_year = 1949)
new_book.delete()
where the first line identify the new_book with the attribute publication_year = 1949
Finally after identifying the object, it is deleted with the comman: new_book.delete()

Expected Output:
Once the object is deleted a retrival command is run to confirm if the object's deletion go through or not


