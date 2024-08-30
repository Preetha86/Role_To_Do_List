from django.db import models

class Stud(models.Model):
    Name = models.CharField(max_length=40)
    Role = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)
    Email = models.CharField(max_length=40)
