from django.db import models

# Create your models here.
class Employee(models.Model):
    nombre = models.CharField(max_lenght=50)
    email = models.CharField(max_lenght=50)
    fono = models.CharField(max_lenght=15)