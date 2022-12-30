from django.db import models
from .Indicator import Indicator

class MeasurementCriterion(models.Model):
    description = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.description} {self.value}"