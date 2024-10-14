from django.db import models

# Create your models here.

class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# To-DO: add class User(models.Model)