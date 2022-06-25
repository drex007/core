from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync 
import json


class College(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)



   

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 