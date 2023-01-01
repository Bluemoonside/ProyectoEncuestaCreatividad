from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics import forms

class VariableUpdateView(UpdateView):
    model = models.Variable
    form_class =forms.VariableForm
    template_name = "updateVariable.html"
    success_url= reverse_lazy('listar_variable')
