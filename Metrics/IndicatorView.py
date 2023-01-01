from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models import models 
from Metrics import forms

def Indicators(request):
    return redirect('/metrics/indicators/')

class IndicatorListView(ListView):
    model =models.Indicator
    template_name = "listIndicator.html"
 
class IndicatorCreateView(CreateView):
    model =models.Indicator
    form_class =forms.IndicatorForm
    template_name = "createdIndicator.html"
    success_url= reverse_lazy('listar_indicator')
    
class IndicatorUpdateView(UpdateView):
    model = models.Indicator
    form_class =forms.IndicatorForm
    template_name = "updateIndicator.html"
    success_url= reverse_lazy('listar_indicator')

class IndicatorDeleteView(DeleteView):
    model = models.Indicator
    template_name = "deleteIndicator.html"
    success_url= reverse_lazy('listar_indicator')