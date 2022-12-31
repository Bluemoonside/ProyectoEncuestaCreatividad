from django.db import models
from .Question import Question

class Poll(models.Model):
    name = models.CharField(max_length=50, default="Encuesta Sin Nombre")
    question = models.ManyToManyField(Question)
    
    def __str__(self):
        return f"Encuesta: {self.id}"