from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from Models import models 

def Dimensions(request):
    return redirect('/metrics/dimensions/')

class DimensionListView(ListView):
    model =models.Dimension
    template_name = "listDimension.html"