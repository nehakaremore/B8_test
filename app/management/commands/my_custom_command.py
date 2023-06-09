# print("in my custom command")

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone

# class Command(BaseCommand):
#     help = 'Displays current time'
#     def handle(self, *args, **kwargs):
#         # print("hi hello")
#         time = timezone.now().strftime('%X')
#         self.stdout.write("It's now %s" % time)

class Command(BaseCommand):
    help = 'Create random users'
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        # print(kwargs)
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=get_random_string(), email='', password='123')
