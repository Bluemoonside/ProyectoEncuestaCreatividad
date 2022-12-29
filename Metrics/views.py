from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView
from Models.models import MeasurementCriterion
from Metrics import forms
# Create your views here.

# creacion de la vista generica para listar MeasurementCriterion
class MeasurementCriterionListView(ListView):
    model =MeasurementCriterion
    template_name = "listMeasurementCriterion.html"
 
