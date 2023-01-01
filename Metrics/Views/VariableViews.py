from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView ,ListView,UpdateView,DeleteView
from Models import models 
from Metrics import forms

def Variables(request):
    return redirect('/metrics/variables/')

class VariableListView(ListView):
    model =models.Variable
    template_name = "listVariable.html"

class VariableCreateView(CreateView):
    model =models.Variable
    form_class =forms.VariableForm
    template_name = "createdVariable.html"
    success_url= reverse_lazy('listar_variable')

class VariableUpdateView(UpdateView):
    model = models.Variable
    form_class =forms.VariableForm
    template_name = "updateVariable.html"
    success_url= reverse_lazy('listar_variable')

class VariableDeleteView(DeleteView):
    model = models.Variable
    template_name = "deleteVariable.html"
    success_url= reverse_lazy('listar_variable')
    