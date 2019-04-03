from django.db import models

class Configuration(models.Model):
    config_id = models.IntegerField(default=1)
    target_frequencies = models.TextField(default='100 200')
    error_threshold = models.IntegerField(default=100)
    angle_offset = models.IntegerField(default=300)
    history = models.IntegerField(default=100)
    active_mics = models.TextField(default='1 2 3 4')

    class Meta:
        ordering = ('config_id',)
