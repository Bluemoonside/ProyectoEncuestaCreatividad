from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics import forms

class MeasurementCriterionUpdateView(UpdateView):
    model = models.MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "updateMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')
