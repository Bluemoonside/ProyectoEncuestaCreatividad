from django.db import models
from .Scale import Scale

class ScaleLabel(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=128, default='')
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE)