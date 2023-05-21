from django.db import models

from staff.models import *


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    staff = models.ForeignKey(to='staff.Staff', on_delete=models.CASCADE)
