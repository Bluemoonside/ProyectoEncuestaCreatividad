from django.db import models

class Variable(models.Model):
    description = models.TextField(default='')
    name = models.CharField(max_length=128, default='')
    class Meta:
        """Meta definition for Variable."""

        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

    def __str__(self):
        """Unicode representation of Variable."""
        pass