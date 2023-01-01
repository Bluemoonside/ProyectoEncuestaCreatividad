from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics import forms

class ScaleUpdateView(UpdateView):
    model = models.Scale
    form_class =forms.ScaleForm
    template_name = "updateScale.html"
    success_url= reverse_lazy('listar_scale')