from django.db import models


# Create your models here.

class Registration(models.Model):
    Username = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    First_name = models.CharField(max_length=25)
    Last_name = models.CharField(max_length=25)
    Location = models.CharField(max_length=25)

    def __str__(self):
        return self.Username
