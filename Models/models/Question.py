from django.db import models
from .MeasurementCriterion import MeasurementCriterion
import datetime

class Question(models.Model):
    TYPE_QUESTION = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    )
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
    type = models.CharField(max_length=1, choices=TYPE_QUESTION, default='')
    measurement_criterion = models.ForeignKey(MeasurementCriterion, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Pregunta: {self.id}"