from django.db import models

class MeasurementCriterion(models.Model):
    description = models.TextField(default='')
    value = models.IntegerField(default=0)
    class Meta:
        """Meta definition for MeasurementCriterion."""
        verbose_name = 'MeasurementCriterion'
        verbose_name_plural = 'MeasurementCriterions'

    def __str__(self):
        """Unicode representation of MeasurementCriterion."""
        pass