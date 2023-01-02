from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 
from Metrics import forms

class ScaleDeleteView(DeleteView):
    model = models.Scale
    template_name = "deleteScale.html"
    success_url= reverse_lazy('listar_scale')