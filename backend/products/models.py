from django.db import models
from user.models import User


# Create your models here.
class Product(models.Model):
    SHAPE_CHOICES = (
        ('triangle', 'triangle'),
        ('rectangle', 'rectangle'),
        ('square', 'square'),
        ('diamond', 'diamond'),
    )

    # title = models.CharField(max_length=120)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES, default="triangle")
    a = models.FloatField(max_length=20, default=-0.1)
    b = models.FloatField(max_length=20, default=-0.1)
    c = models.FloatField(max_length=20, default=-0.1)

