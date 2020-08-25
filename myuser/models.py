from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    displayname = models.CharField(max_length=100, default="")
    age = models.IntegerField(blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    