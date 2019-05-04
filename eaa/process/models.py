from django.db import models

class Process(models.Model):
    proc_id = models.IntegerField(default=1)
    option = models.TextField(default='restart')

    class Meta:
        ordering = ('proc_id')
