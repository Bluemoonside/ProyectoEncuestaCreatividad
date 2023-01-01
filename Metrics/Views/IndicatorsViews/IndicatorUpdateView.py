from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics import forms


 

    
class IndicatorUpdateView(UpdateView):
    model = models.Indicator
    form_class =forms.IndicatorForm
    template_name = "updateIndicator.html"
    success_url= reverse_lazy('listar_indicator')

