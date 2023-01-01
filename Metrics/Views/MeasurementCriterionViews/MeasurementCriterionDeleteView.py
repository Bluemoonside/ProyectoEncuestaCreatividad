from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 
from Metrics import forms

class MeasurementCriterionDeleteView(DeleteView):
    model = models.MeasurementCriterion
    template_name = "deleteMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')