from django.db import models

class Configuration(models.Model):
    configId = models.IntegerField(default=1)
    targetFrequencies = models.TextField(default='100,200')
    errorThreshold = models.TextField(default='10')
    isDarkMode = models.TextField(default='0')

    class Meta:
        ordering = ('configId',)
