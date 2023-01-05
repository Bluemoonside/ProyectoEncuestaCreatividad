from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from Models import models 
from Metrics import forms

class VariableCreateView(CreateView):
    model =models.Variable
    form_class =forms.VariableForm
    template_name = "createdVariable.html"
    success_url= reverse_lazy('listar_dimension')