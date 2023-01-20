from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics.Forms.DimensionForm import DimensionForm

class DimensionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Dimension
    form_class = DimensionForm
    template_name = "updateDimension.html"
    success_url= reverse_lazy('listar_dimension')
    permission_required = 'Models.change_dimension'
    permission_denied_message = 'Usuario No Autorizado'