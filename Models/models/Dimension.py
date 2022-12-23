from django.db import models

class Dimension(models.Model):
    description = models.TextField(default='')
    weigh = models.IntegerField(default=0)
    class Meta:
        """Meta definition for Dimension."""

        verbose_name = 'Dimension'
        verbose_name_plural = 'Dimensions'

    def __str__(self):
        """Unicode representation of Dimension."""
        pass
