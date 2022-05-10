from django.db import models


# Create your models here.
class User(models.Model):
    # unique=True user name is unique
    user_name = models.CharField(max_length=32, unique=True)
    user_password = models.CharField(max_length=256)
    is_delete = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
