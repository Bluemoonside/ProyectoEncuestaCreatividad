from django.shortcuts import render
from Models.models import Poll
from django.urls import reverse_lazy 
from django.views.generic import DeleteView


class PollDelete(DeleteView):
    model = Poll
    template_name = 'deletepoll.html'
    success_url = reverse_lazy('polllist')
