from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 


class DimensionDeleteView(DeleteView):
    model = models.Dimension
    template_name = "deleteDimension.html"
    success_url= reverse_lazy('listar_dimension')