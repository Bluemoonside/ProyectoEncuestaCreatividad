from django.db import models

class Scale(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=128, default='')
    max_value = models.IntegerField(default=0)
    min_value = models.IntegerField(default=0) 
    interval = models.IntegerField(default=0)
