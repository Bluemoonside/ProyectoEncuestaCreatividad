from django.db import models
from .Indicator import Indicator

class MeasurementCriterion(models.Model):
    description = models.TextField(default='')
    value = models.IntegerField(default=0)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True)
    class Meta:
        """Meta definition for MeasurementCriterion."""
        verbose_name = 'MeasurementCriterion'
        verbose_name_plural = 'MeasurementCriterions'

    def __str__(self):
        """Unicode representation of MeasurementCriterion."""
        pass