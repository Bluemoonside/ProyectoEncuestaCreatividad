from django.db import models
from .Poll import Poll

class Respondent(models.Model):
    polls = models.ManyToManyField(Poll)
    class Meta:
        """Meta definition for Respondent."""

        verbose_name = 'Respondent'
        verbose_name_plural = 'Respondents'

    def __str__(self):
        """Unicode representation of Respondent."""
        pass