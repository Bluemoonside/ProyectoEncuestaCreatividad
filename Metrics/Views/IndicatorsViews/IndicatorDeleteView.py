from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 

class IndicatorDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.Indicator
    template_name = "deleteIndicator.html"
    success_url= reverse_lazy('listar_indicator')
    permission_required = 'Models.delete_indicator'
    permission_denied_message = 'Usuario No Autorizado'