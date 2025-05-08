from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length = 200)

    completed = models.BooleanField(default = False)