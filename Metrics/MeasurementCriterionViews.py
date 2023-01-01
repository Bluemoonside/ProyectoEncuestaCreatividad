from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models import models 
from Metrics import forms

def MeasurementCriterions(request):
    return redirect('/metrics/measurementcriterions/')

class MeasurementCriterionListView(ListView):
    model =models.MeasurementCriterion
    template_name = "listMeasurementCriterion.html"
 
class MeasurementCriterionCreateView(CreateView):
    model =models.MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "createdMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio') 
    
class MeasurementCriterionUpdateView(UpdateView):
    model = models.MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "updateMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')

class MeasurementCriterionDeleteView(DeleteView):
    model = models.MeasurementCriterion
    template_name = "deleteMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')