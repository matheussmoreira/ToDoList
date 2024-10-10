from django.db import models

# Create your models here.

from django.db import models

class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=180)
    details = models.CharField(max_length=300)
    is_checked = models.BooleanField(default=False)
    deadline = models.DateField()

    def __str__(self):
        return self.name

# TO-DO: add class Category(models.Model)
# To-DO: add class User(models.Model)