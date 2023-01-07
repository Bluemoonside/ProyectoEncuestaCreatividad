from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Models import models 
from Metrics.Forms.MeasurementCriterionForm import MeasurementCriterionForm

class MeasurementCriterionCreateView(CreateView):
    model =models.MeasurementCriterion
    form_class = MeasurementCriterionForm
    template_name = "createdMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio') 
    