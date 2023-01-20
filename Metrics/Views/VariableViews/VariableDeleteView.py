from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from Models import models 


class VariableDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = models.Variable
    template_name = "deleteVariable.html"
    success_url= reverse_lazy('listar_variable')
    permission_required = 'Models.delete_variable'
    permission_denied_message = 'Usuario No Autorizado'