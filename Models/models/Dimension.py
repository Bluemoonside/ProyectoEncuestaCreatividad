from django.db import models
from .Variable import Variable
from .Scale import Scale

class Dimension(models.Model):
    description = models.CharField(max_length=200)
    weigh = models.IntegerField(default=0)
    variables = models.ManyToManyField(Variable)
    scale = models.ForeignKey(Scale, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dimension({self.id}): {self.description}"