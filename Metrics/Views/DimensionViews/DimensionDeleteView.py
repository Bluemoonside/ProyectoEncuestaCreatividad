from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models import models 


class DimensionDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    model = models.Dimension
    template_name = "deleteDimension.html"
    success_url= reverse_lazy('listar_dimension')
    permission_required = 'Models.delete_dimension'
    permission_denied_message = 'Usuario No Autorizado'