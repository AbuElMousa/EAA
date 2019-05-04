from django.db import models

class Sound(models.Model):
    time = models.TextField(default='1')
    frequency = models.TextField(default='1')
    amplitude = models.TextField(default='1')
    direction = models.TextField(default='1')

    class Meta:
        ordering = ('time','frequency','amplitude','direction')
