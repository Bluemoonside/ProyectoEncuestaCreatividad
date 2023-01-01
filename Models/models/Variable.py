from django.db import models
from .Scale import Scale

class Variable(models.Model):
    description = models.CharField(max_length=200)
    name = models.CharField(max_length=128, default='')
    scale = models.OneToOneField(Scale, on_delete=models.CASCADE, parent_link=True, null=True)