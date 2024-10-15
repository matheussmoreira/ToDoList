from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    todos = list()

    def __str__(self):
        return self.username