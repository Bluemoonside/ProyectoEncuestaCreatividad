from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from Models import models 
from Metrics.Forms.MeasurementCriterionForm import MeasurementCriterionForm

class MeasurementCriterionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model =models.MeasurementCriterion
    form_class = MeasurementCriterionForm
    template_name = "createdMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio') 
    permission_required = 'Models.add_measurementcriterion'
    permission_denied_message = 'Usuario No Autorizado'