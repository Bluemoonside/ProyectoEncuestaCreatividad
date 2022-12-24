from django.db import models
from .Indicator import Indicator
from .Scale import Scale

class Dimension(models.Model):
    description = models.CharField(max_length=200)
    weigh = models.IntegerField(default=0)
    indicators = models.ManyToManyField(Indicator)
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE, parent_link=True, null=True)
