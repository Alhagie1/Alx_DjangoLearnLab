from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book,CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publication_year"]
    list_filter = ["publication_year"]
    search_fields = ["title", "author"]
admin.site.register(Book,BookAdmin)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)