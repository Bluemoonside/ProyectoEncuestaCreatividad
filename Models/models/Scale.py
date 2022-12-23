from django.db import models

class Scale(models.Model):
    description = models.TextField(default='')
    name = models.CharField(max_length=128, default='')
    maxValue = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)
    minValue = models.IntegerField(default=0)
    class Meta:
        """Meta definition for Scale."""

        verbose_name = 'Scale'
        verbose_name_plural = 'Scales'

    def __str__(self):
        """Unicode representation of Scale."""
        pass