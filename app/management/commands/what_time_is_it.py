from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.utils import timezone

class Command(BaseCommand):
    help = 'Displays current time'
    def handle(self, *args, **kwargs):
        # print("hi hello")
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)
        