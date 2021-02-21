from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 20)
    code = models.IntegerField()

class Publication(models.Model):
    user = models.CharField(max_length = 20)
    text = models.CharField(max_length = 250, default = None)
    image = models.ImageField(default = None)
    date = models.DateTimeField()