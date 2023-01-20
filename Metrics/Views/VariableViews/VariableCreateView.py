from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView 
from Models import models 
from Metrics.Forms.VariableForm import VariableForm 

class VariableCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model =models.Variable
    form_class = VariableForm
    template_name = "createdVariable.html"
    success_url= reverse_lazy('listar_dimension')
    permission_required = 'Models.add_variable'
    permission_denied_message = 'Usuario No Autorizado'