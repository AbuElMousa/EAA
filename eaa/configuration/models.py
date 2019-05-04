from django.db import models

class Configuration(models.Model):
    configId = models.IntegerField(default=1)
    targetFrequencies = models.TextField(default='100 200')
    errorThreshold = models.IntegerField(default=100)
    isDarkMode = models.IntegerField(default=0)

    class Meta:
        ordering = ('configId',)
