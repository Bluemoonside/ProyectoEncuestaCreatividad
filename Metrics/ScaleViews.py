from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models import models 
from Metrics import forms

class ScaleListView(ListView):
    model =models.Scale
    template_name = "listScale.html"

class ScaleCreateView(CreateView):
    model =models.Scale
    form_class =forms.ScaleForm
    template_name = "createdScale.html"
    success_url= reverse_lazy('listar_scale')

class ScaleUpdateView(UpdateView):
    model = models.Scale
    form_class =forms.ScaleForm
    template_name = "updateScale.html"
    success_url= reverse_lazy('listar_scale')

class ScaleDeleteView(DeleteView):
    model = models.Scale
    template_name = "deleteScale.html"
    success_url= reverse_lazy('listar_scale')
    