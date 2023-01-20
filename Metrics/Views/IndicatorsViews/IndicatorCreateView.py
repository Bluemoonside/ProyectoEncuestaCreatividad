from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models import models 
from Metrics.Forms.IndicatorForm import IndicatorForm


class IndicatorCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model =models.Indicator
    form_class = IndicatorForm
    template_name = "createdIndicator.html"
    success_url= reverse_lazy('listar_criterio')
    permission_required = 'Models.add_indicator'
    permission_denied_message = 'Usuario No Autorizado'