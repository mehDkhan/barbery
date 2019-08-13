from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    location = models.CharField(max_length=50,blank=True,null=True)
    bio = models.CharField(max_length=280,blank=True,null=True)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.username
