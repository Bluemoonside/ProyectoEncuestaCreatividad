from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics.Forms.MeasurementCriterionForm import MeasurementCriterionForm 

class MeasurementCriterionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.MeasurementCriterion
    form_class = MeasurementCriterionForm
    template_name = "updateMeasurementCriterion.html"
    success_url= reverse_lazy('listar_criterio')
    permission_required = 'Models.change_measurementcriterion'
    permission_denied_message = 'Usuario No Autorizado'
