
# Create your models here.
from __future__ import unicode_literals

from django.db import models

class Destinations(models.Model):
    id = models.IntegerField(primary_key=True)
    cityname = models.TextField(db_column='CityName', blank=True) # Field name made lowercase. This field type is a guess.
    airport = models.TextField(db_column='Airport', blank=True) # Field name made lowercase. This field type is a guess.
    lat = models.TextField(db_column='Lat', blank=True) # Field name made lowercase. This field type is a guess.
    lon = models.TextField(db_column='Lon', blank=True) # Field name made lowercase. This field type is a guess.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'destinations'



class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)