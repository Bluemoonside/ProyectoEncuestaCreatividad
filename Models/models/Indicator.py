from django.db import models
from .Scale import Scale

class Indicator(models.Model):
    description = models.CharField(max_length=200)
    weigh = models.IntegerField(default=0)
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE, parent_link=True, null=True)