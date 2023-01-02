from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from Models import models 
from Metrics import forms

def Variables(request):
    return redirect('/metrics/variables/')

class VariableListView(ListView):
    model =models.Variable
    template_name = "listVariable.html"





    