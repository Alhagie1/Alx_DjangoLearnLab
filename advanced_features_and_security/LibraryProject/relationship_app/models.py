from django.db import models
from django.contrib.auth.models import User, AbstractUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.conf import settings
Role_Choices = (
    ("Admin", "Admin"),
    ("Librarian", "Librarian"),
    ("Member", "Member"),
)
class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) 
    role = models.CharField(max_length= 100, choices = Role_Choices)
    
    def __str__(self):
        return self.user
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']
    def __str__(self):
        return self.email

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be found")
        email = self.normalize_email(email)
        user = self.model(email = email)
        user.set_password(password)
        user.save(using = self._db)
        return self.create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault(staff = True)
        extra_fields.setdefault(active = True)
        extra_fields.setdefault(is_superuser = True)
        if extra_fields.get("is-staff") is not True:
            raise ValueError("superuser must have is_staff = True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must get is_superuser = True")
        return self.create_superuser(email, password, **extra_fields)
    





