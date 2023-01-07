from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from Models import models 


def MeasurementCriterions(request):
    return redirect('/metrics/measurementcriterions/')

class MeasurementCriterionListView(ListView):
    model =models.MeasurementCriterion
    template_name = "listMeasurementCriterion.html"



