from django.db import models
from .Ask import Ask

class Poll(models.Model):
    asks = models.ManyToManyField(Ask)
    class Meta:
        """Meta definition for Poll."""

        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __str__(self):
        """Unicode representation of Poll."""
        pass