import os

from django.db import models


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'CAR'

    name = models.CharField(max_length=30)
    year = models.IntegerField()
    image = models.ImageField(upload_to=os.path.join('car', 'img'), default='', blank=True)
