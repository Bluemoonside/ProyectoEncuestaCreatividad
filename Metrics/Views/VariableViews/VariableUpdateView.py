from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models import models 
from Metrics.Forms.VariableForm import VariableForm

class VariableUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = models.Variable
    form_class = VariableForm
    template_name = "updateVariable.html"
    success_url= reverse_lazy('listar_variable')
    permission_required = 'Models.change_variable'
    permission_denied_message = 'Usuario No Autorizado'
