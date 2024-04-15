from django.db import models


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
