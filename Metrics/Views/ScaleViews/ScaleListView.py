from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from Models import models 


class ScaleListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model =models.Scale
    template_name = "listScale.html"
    permission_required = 'Models.view_scale'
    permission_denied_message = 'Usuario No Autorizado'






    