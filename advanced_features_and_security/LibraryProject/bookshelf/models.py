from django.db import models
from django.db import models
from django.contrib.auth.models import User, AbstractUser,BaseUserManager
from django.contrib.auth.models import Permission
from django.conf import settings
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class Post(models.Model):
    class Meta:
        permissions = [
            ("can_view ", "can view"),
            ("can_create", "can create"),
            ("can_edit", "can edit"),
            ("can_delete", "can delete"),

        ]
    
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


