#from django.db import models
from django.contrib.gis.db import models


class RoadNetwork(models.Model):
    geometry = models.LineStringField(srid=25832)
    max_speed = models.IntegerField()

# Create your models here.
