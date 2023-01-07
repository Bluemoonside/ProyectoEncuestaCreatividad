from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Models import models 
from Metrics.Forms.IndicatorForm import IndicatorForm


class IndicatorCreateView(CreateView):
    model =models.Indicator
    form_class = IndicatorForm
    template_name = "createdIndicator.html"
    success_url= reverse_lazy('listar_criterio')