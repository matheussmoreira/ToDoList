from django.db import models
from django.contrib.auth.models import AbstractUser

class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    is_checked = models.BooleanField(default=False)
    user = models.ForeignKey('CustomUser', related_name='todos', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    pass  
