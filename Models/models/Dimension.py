from django.db import models
from .Variable import Variable
from .Scale import Scale

class Dimension(models.Model):
    description = models.CharField(max_length=200)
    weigh = models.IntegerField(default=0)
    variables = models.ManyToManyField(Variable)
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE, parent_link=True, null=True)
