from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 


class MeasurementCriterionDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.MeasurementCriterion
    template_name = "deleteMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')
    permission_required = 'Models.delete_measurementcriterion'
    permission_denied_message = 'Usuario No Autorizado'