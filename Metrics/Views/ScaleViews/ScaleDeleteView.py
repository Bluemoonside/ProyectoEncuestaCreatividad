from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 


class ScaleDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.Scale
    template_name = "deleteScale.html"
    success_url= reverse_lazy('listar_scale')
    permission_required = 'Models.delete_scale'
    permission_denied_message = 'Usuario No Autorizado'