from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models import models 
from Metrics import forms
# Create your views here.
#Metodos para direccionar a las difrerntes gestiones de tablas
def Indicators(request):
    return redirect('/metrics/indicators/')
def MeasurementCriterions(request):
    return redirect('/metrics/measurementcriterions/')
def Dimensions(request):
    return redirect('/metrics/dimensions/')

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

# creacion de la vista generica para listar Scale
class ScaleListView(ListView):
    model =models.Scale
    template_name = "listScale.html"

# creacion de la vista generica para crear Scale
class ScaleCreateView(CreateView):
    model =models.Scale
    form_class =forms.ScaleForm
    template_name = "createdScale.html"
    success_url= reverse_lazy('listar_scale')
    
# creacion de la vista generica para editar Scale
class ScaleUpdateView(UpdateView):
    model = models.Scale
    form_class =forms.ScaleForm
    template_name = "updateScale.html"
    success_url= reverse_lazy('listar_scale')

# creacion de la vista generica para eliminar Scale
class ScaleDeleteView(DeleteView):
    model = models.Scale
    template_name = "deleteScale.html"
    success_url= reverse_lazy('listar_scale')
    
# creacion de la vista generica para listar Dimension
class DimensionListView(ListView):
    model =models.Dimension
    template_name = "listDimension.html"
 
# creacion de la vista generica para crear Dimension
class DimensionCreateView(CreateView):
    model =models.Dimension
    form_class =forms.DimensionForm
    template_name = "createdDimension.html"
    success_url= reverse_lazy('listar_dimension')
    
# creacion de la vista generica para editar Dimension
class DimensionUpdateView(UpdateView):
    model = models.Dimension
    form_class =forms.DimensionForm
    template_name = "updateDimension.html"
    success_url= reverse_lazy('listar_dimension')

# creacion de la vista generica para eliminar Dimension
class DimensionDeleteView(DeleteView):
    model = models.Dimension
    template_name = "deleteDimension.html"
    success_url= reverse_lazy('listar_dimension')
