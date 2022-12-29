from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models import models 
from Metrics import forms
# Create your views here.
#Metodos para direccionar a las difrerntes grstiones de tablas
def Indicators(request):
    return redirect('/Metrics/listIndicator/')
def MeasurementCriterions(request):
    return redirect('/Metrics/listMeasurementCriterion/')

# creacion de la vista generica para listar MeasurementCriterion
class MeasurementCriterionListView(ListView):
    model =models.MeasurementCriterion
    template_name = "listMeasurementCriterion.html"
 
 # creacion de la vista generica para crear MeasurementCriterion
class MeasurementCriterionCreateView(CreateView):
    model =models.MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "createdMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')
    
# creacion de la vista generica para editar MeasurementCriterion
class MeasurementCriterionUpdateView(UpdateView):
    model = models.MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "updateMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')

# creacion de la vista generica para eliminar MeasurementCriterion
class MeasurementCriterionDeleteView(DeleteView):
    model = models.MeasurementCriterion
    template_name = "deleteMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')

# creacion de la vista generica para listar Indicator
class IndicatorListView(ListView):
    model =models.Indicator
    template_name = "listIndicator.html"
 
# creacion de la vista generica para crear Indicator
class IndicatorCreateView(CreateView):
    model =models.Indicator
    form_class =forms.IndicatorForm
    template_name = "createdIndicator.html"
    success_url= reverse_lazy('listar_indicator')
    
# creacion de la vista generica para editar Indicator
class IndicatorUpdateView(UpdateView):
    model = models.Indicator
    form_class =forms.IndicatorForm
    template_name = "updateIndicator.html"
    success_url= reverse_lazy('listar_indicator')

# creacion de la vista generica para eliminar Indicator
class IndicatorDeleteView(DeleteView):
    model = models.Indicator
    template_name = "deleteIndicator.html"
    success_url= reverse_lazy('listar_indicator')