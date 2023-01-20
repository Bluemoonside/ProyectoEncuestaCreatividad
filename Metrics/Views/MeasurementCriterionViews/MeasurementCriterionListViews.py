from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from Models import models 


def MeasurementCriterions(request):
    return redirect('/metrics/measurementcriterions/')

class MeasurementCriterionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model =models.MeasurementCriterion
    template_name = "listMeasurementCriterion.html"
    permission_required = 'Models.view_measurementcriterion'
    permission_denied_message = 'Usuario No Autorizado'



