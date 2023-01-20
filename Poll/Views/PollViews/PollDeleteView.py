from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models.models import Poll
from django.urls import reverse_lazy 
from django.views.generic import DeleteView


class PollDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Poll
    template_name = 'deletepoll.html'
    success_url = reverse_lazy('polllist')
    permission_required = 'Models.delete_poll'
    permission_denied_message = 'Usuario No Autorizado'
