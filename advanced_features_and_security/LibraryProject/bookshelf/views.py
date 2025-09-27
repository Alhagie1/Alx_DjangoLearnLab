from django.shortcuts import render
from django.contrib.auth.models import Group, Permission
def index(request):
    return render(request, 'booshelf/')

editors = Group.objects.get(name= "Editors")
viewers = Group.objects.get(name="Viewers")
admins = Group.objects.get(name="Admins")

editors_group = Permission.objects.filter(codename__in=[
    ("can_edit"),
    ("can_create"),
   ("can_view") ,
   ("can_add")
])

viewers_group = Permission.objects.filter(codename=("can_view", ),
)

admins_group = Permission.objects.all()

editors.permissions.set(editors_group)
viewers.permissions.set(viewers_group)
admins.permissions.set(admins_group)

print("group permissions created successfully.")