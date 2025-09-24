from django.db import models

# This is the Author model with an attribute name

class Author(models.Model):
    name = models.CharField(max_length=64)

# This is the book model 
class Book:
    title = models.CharField(max_length=64)
    publication_year = models.IntegerField()
    # This is one to many relationship with the foreign key from author to Book model
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
