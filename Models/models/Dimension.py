from django.db import models
from .Indicator import Indicator
from .Scale import Scale

class Dimension(models.Model):
    description = models.TextField(default='')
    weigh = models.IntegerField(default=0)
    indicators = models.ManyToManyField(Indicator)
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE, parent_link=True)
    class Meta:
        """Meta definition for Dimension."""

        verbose_name = 'Dimension'
        verbose_name_plural = 'Dimensions'

    def __str__(self):
        """Unicode representation of Dimension."""
        pass
