from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default=False)

# class ExtendedUser(models.Model):
#     mob = models.CharField(max_length=100, null=True)
#     adre = models.FloatField()
#     age = models.IntegerField()
#     user = models.OneToOneField(User)

    class Meta:
        db_table = "book"

