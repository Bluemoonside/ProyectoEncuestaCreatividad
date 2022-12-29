from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models.models import MeasurementCriterion
from Metrics import forms
# Create your views here.

# creacion de la vista generica para listar MeasurementCriterion
class MeasurementCriterionListView(ListView):
    model =MeasurementCriterion
    template_name = "listMeasurementCriterion.html"
 
 # creacion de la vista generica para crear MeasurementCriterion
class MeasurementCriterionCreateView(CreateView):
    model =MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "createdMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')
    
# creacion de la vista generica para editar MeasurementCriterion
class MeasurementCriterionUpdateView(UpdateView):
    model = MeasurementCriterion
    form_class =forms.MeasurementCriterionForm
    template_name = "createdMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')

# creacion de la vista generica para eliminar MeasurementCriterion
class MeasurementCriterionDeleteView(DeleteView):
    model = MeasurementCriterion
    template_name = "deleteMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')
