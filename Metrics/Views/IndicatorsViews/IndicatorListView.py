from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from Models import models 

def Indicators(request):
    return redirect('/metrics/indicators/')

class IndicatorListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model =models.Indicator
    template_name = "listIndicator.html"
    permission_required = 'Models.view_indicator'
    permission_denied_message = 'Usuario No Autorizado'