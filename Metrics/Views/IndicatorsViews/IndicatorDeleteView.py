from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 

class IndicatorDeleteView(DeleteView):
    model = models.Indicator
    template_name = "deleteIndicator.html"
    success_url= reverse_lazy('listar_indicator')