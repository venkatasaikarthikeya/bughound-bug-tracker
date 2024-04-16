from django.db import models
from django.contrib.auth.models import User


roles = [
    ('Admin', 'Admin'),
    ('User', 'User'),
    ('Manager', 'Manager')
]


class Program(models.Model):
    
    name = models.CharField(max_length=100)

    version = models.CharField(max_length=100)

    release = models.CharField(max_length=100)

    def __str__(self):
        return self.name + '  ' + self.version + '  ' + self.release
    

class FunctionalArea(models.Model):
    
    name = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return self.name + '   ' + self.description
    

class Employee(models.Model):

    name = models.CharField(max_length=100, default='')

    email = models.CharField(max_length=100, default='')

    role = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '  ' + self.email + '  ' + self.role
