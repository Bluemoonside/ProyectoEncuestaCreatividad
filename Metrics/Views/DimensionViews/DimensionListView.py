from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from Models import models 

def Dimensions(request):
    return redirect('/metrics/dimensions/')

class DimensionListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model =models.Dimension
    template_name = "listDimension.html"
    permission_required = 'Models.view_dimension'
    permission_denied_message = 'Usuario No Autorizado'