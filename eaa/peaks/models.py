from django.db import models

class Peak(models.Model):
    peak_id = models.IntegerField(default=1)
    top_left = models.IntegerField(default=-1)
    bottom_left = models.IntegerField(default=-1)

    class Meta:
        ordering = ('peak_id')
