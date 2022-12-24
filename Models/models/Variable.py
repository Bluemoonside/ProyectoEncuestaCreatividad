from django.db import models
from .Dimension import Dimension
from .Scale import Scale

class Variable(models.Model):
    description = models.TextField(default='')
    name = models.CharField(max_length=128, default='')
    dimensions = models.ManyToManyField(Dimension)
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE, parent_link=True, null=True)
    class Meta:
        """Meta definition for Variable."""

        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

    def __str__(self):
        """Unicode representation of Variable."""
        pass