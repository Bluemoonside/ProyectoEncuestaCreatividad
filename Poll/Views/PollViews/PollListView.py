from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models.models import Poll
from django.views.generic import ListView


class PollList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Poll
    template_name = 'polllist.html'
    permission_required = 'Models.view_poll'
    permission_denied_message = 'Usuario No Autorizado'