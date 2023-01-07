from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics.Forms.DimensionForm import DimensionForm

class DimensionUpdateView(UpdateView):
    model = models.Dimension
    form_class = DimensionForm
    template_name = "updateDimension.html"
    success_url= reverse_lazy('listar_dimension')