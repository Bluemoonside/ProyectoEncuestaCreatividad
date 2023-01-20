from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models.models import Poll
from Poll.Forms.PollForm import PollForm
from django.urls import reverse_lazy 
from django.views.generic import UpdateView


class PollUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'updatepoll.html'
    success_url = reverse_lazy('polllist')
    permission_required = 'Models.change_poll'
    permission_denied_message = 'Usuario No Autorizado'