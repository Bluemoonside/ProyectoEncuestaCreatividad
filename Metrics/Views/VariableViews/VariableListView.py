from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from Models import models 


def Variables(request):
    return redirect('/metrics/variables/')

class VariableListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model =models.Variable
    template_name = "listVariable.html"
    permission_required = 'Models.view_variable'
    permission_denied_message = 'Usuario No Autorizado'

