import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Member (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)





class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Notes(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,  null=True, blank=True)

    def __str__(self):
        return self.title








