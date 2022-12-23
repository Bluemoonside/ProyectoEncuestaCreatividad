from django.db import models
from .Scale import Scale

class Indicator(models.Model):
    description = models.TextField(default='')
    weigh = models.IntegerField(default=0)
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE, parent_link=True)
    class Meta:
        """Meta definition for Indicator."""

        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'

    def __str__(self):
        """Unicode representation of Indicator."""
        pass