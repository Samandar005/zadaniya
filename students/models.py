from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_birth = models.DateField()
    gender = models.CharField(max_length=25)
    address = models.TextField()