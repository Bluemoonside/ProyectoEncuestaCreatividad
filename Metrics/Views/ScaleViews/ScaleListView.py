from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from Models import models 


class ScaleListView(ListView):
    model =models.Scale
    template_name = "listScale.html"






    