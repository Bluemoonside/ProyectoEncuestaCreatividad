from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Models import models 
from Metrics import forms

class MeasurementCriterionCreateView(CreateView):
    model =models.MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "createdMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio') 
    