from django.db import models


# Create your models here.
class User(models.Model):
    us_name = models.CharField(max_length = 20)
    us_password = models.CharField(max_length = 20)
    def __str__(self):
        return self.us_name

class Publication(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length = 20)
    text = models.CharField(max_length = 250, default = None)
    image = models.ImageField()
    date = models.DateTimeField()