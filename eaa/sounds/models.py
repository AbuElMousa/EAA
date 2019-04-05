from django.db import models

class Sound(models.Model):
    time = models.IntegerField(default=-1)
    frequency = models.IntegerField(default=-1)
    amplitude = models.IntegerField(default=-1)
    direction = models.IntegerField(default=-1)

    class Meta:
        ordering = ('time',)
