from django.db import models
from .Question import Question

class Poll(models.Model):
    question = models.ManyToManyField(Question)
    
    def __str__(self):
        return f"Encuesta {self.id}"