from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics.Forms.IndicatorForm import IndicatorForm


class IndicatorUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Indicator
    form_class = IndicatorForm
    template_name = "updateIndicator.html"
    success_url= reverse_lazy('listar_indicator')
    permission_required = 'Models.change_indicator'
    permission_denied_message = 'Usuario No Autorizado'

