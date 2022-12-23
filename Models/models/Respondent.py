from django.db import models

class Respondent(models.Model):
    """Model definition for Respondent."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Respondent."""

        verbose_name = 'Respondent'
        verbose_name_plural = 'Respondents'

    def __str__(self):
        """Unicode representation of Respondent."""
        pass