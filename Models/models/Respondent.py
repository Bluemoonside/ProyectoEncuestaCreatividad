from django.db import models
from .Poll import Poll

class Respondent(models.Model):
    polls = models.ManyToManyField(Poll)