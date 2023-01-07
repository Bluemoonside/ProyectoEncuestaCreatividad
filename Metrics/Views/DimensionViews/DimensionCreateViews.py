from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Models import models 
from Metrics.Forms.DimensionForm import DimensionForm


class DimensionCreateView(CreateView):
    model =models.Dimension
    form_class = DimensionForm
    template_name = "createdDimension.html"
    success_url= reverse_lazy('listar_indicator')