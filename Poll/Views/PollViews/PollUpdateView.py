from django.shortcuts import render
from Models.models import Poll
from Poll.Forms.PollForm import PollForm
from django.urls import reverse_lazy 
from django.views.generic import UpdateView


class PollUpdate(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'updatepoll.html'
    success_url = reverse_lazy('polllist')