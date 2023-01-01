from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from Models import models 
from Metrics import forms

class ScaleCreateView(CreateView):
    model =models.Scale
    form_class =forms.ScaleForm
    template_name = "createdScale.html"
    success_url= reverse_lazy('listar_scale')