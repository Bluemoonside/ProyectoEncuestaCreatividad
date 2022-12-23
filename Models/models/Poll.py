from django.db import models

class Poll(models.Model):
    """Model definition for Poll."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Poll."""

        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __str__(self):
        """Unicode representation of Poll."""
        pass