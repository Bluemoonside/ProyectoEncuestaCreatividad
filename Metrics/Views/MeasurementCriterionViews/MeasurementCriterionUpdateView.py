from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics.Forms.MeasurementCriterionForm import MeasurementCriterionForm 

class MeasurementCriterionUpdateView(UpdateView):
    model = models.MeasurementCriterion
    form_class = MeasurementCriterionForm
    template_name = "updateMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')
