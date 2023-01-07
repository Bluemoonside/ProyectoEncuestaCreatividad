from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from Models import models 

def Indicators(request):
    return redirect('/metrics/indicators/')

class IndicatorListView(ListView):
    model =models.Indicator
    template_name = "listIndicator.html"