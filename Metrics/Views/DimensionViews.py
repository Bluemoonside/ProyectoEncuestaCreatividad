from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models import models 
from Metrics import forms

def Dimensions(request):
    return redirect('/metrics/dimensions/')
class DimensionListView(ListView):
    model =models.Dimension
    template_name = "listDimension.html"
 
class DimensionCreateView(CreateView):
    model =models.Dimension
    form_class =forms.DimensionForm
    template_name = "createdDimension.html"
    success_url= reverse_lazy('listar_dimension')

class DimensionUpdateView(UpdateView):
    model = models.Dimension
    form_class =forms.DimensionForm
    template_name = "updateDimension.html"
    success_url= reverse_lazy('listar_dimension')

class DimensionDeleteView(DeleteView):
    model = models.Dimension
    template_name = "deleteDimension.html"
    success_url= reverse_lazy('listar_dimension')