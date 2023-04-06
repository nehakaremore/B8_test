# exec(open(r'C:\Users\shubham karemore\Desktop\Neha Folder\Python Class\B8_Django\LibraryProj\app\db_shell.py').read())

from django.contrib.auth.models import User, Group

# print(User.objects.all())   # <QuerySet [<User: Neha>, <User: nehakaremore12@gmail.com>]>

# To create User
# User.objects.create_user(username="Dinesh", password="Python@123", email="d@gmail.com")

# User.objects.create(username="Dinesh1", password="Python@123", email="d1@gmail.com")

# from django.utils.crypto import get_random_string

# print(get_random_string())

from django.contrib.auth.models import User
# user = User.objects.get(id=1)
user = User.objects.get(id=1).profile
user = User.objects.get(id=1).profile.location


print(user)