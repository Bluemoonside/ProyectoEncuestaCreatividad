from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Models import models 
from Metrics.Forms.ScaleForm import ScaleForm 

class ScaleUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Scale
    form_class = ScaleForm
    template_name = "updateScale.html"
    success_url= reverse_lazy('listar_scale')
    permission_required = 'Models.change_scale'
    permission_denied_message = 'Usuario No Autorizado'