from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics.Forms.IndicatorForm import IndicatorForm


class IndicatorUpdateView(UpdateView):
    model = models.Indicator
    form_class = IndicatorForm
    template_name = "updateIndicator.html"
    success_url= reverse_lazy('listar_indicator')

