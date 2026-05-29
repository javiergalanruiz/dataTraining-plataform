from django.db import models

# Create your models here.
from django.db import models


class GPSPoint(models.Model):
    player_id = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    speed = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField()
