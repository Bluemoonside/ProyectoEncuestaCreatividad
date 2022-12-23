from django.db import models
from .MeasurementCriterion import MeasurementCriterion

class Ask(models.Model):
    TYPE_QUESTION = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    type = models.CharField(max_length=1, choices=TYPE_QUESTION, default='')
    question = models.TextField(default='')
    answer = models.TextField(default='')
    measurementCriterion = models.ForeignKey(MeasurementCriterion, on_delete=models.CASCADE, null=True)
    class Meta:
        """Meta definition for Ask."""

        verbose_name = 'Ask'
        verbose_name_plural = 'Asks'

    def __str__(self):
        """Unicode representation of Ask."""
        pass