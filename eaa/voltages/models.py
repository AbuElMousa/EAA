from django.db import models

class Voltage(models.Model):
    volt_id = models.IntegerField(default=1)
    top_left = models.TextField(default='1 2 3')
    bottom_left = models.TextField(default='1 2 3')

    class Meta:
        ordering = ('volt_id')
