from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from Models import models 
from Metrics.Forms.ScaleForm import ScaleForm 

class ScaleCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model =models.Scale
    form_class = ScaleForm
    template_name = "createdScale.html"
    success_url= reverse_lazy('listar_scale')
    permission_required = 'Models.add_scale'
    permission_denied_message = 'Usuario No Autorizado'