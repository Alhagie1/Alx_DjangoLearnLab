update in databases
This is a process in which records of database objects are modified 

command: 
new_book = Book.object.get(title = "1984")
new_book.title = "Nineteen Eighty-Four"
new_book.save()

where,
new_book = the database object
title = "1984": This is the identifier of the object new_book
new_book.title  = "Nineteen Eighty-Four": This line modify the title value from "1984" to "Nineteen Eighty-Four"

new_book.save(): Finally the updated record is save to the database object.

Ecpected Output:
After running this command the title of the new_book object is change to "Nineteen Eighty-Four"

