from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 
from Metrics import forms

class VariableDeleteView(DeleteView):
    model = models.Variable
    template_name = "deleteVariable.html"
    success_url= reverse_lazy('listar_variable')