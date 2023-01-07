from django.shortcuts import render
from Models.models import Poll
from django.views.generic import ListView


class PollList(ListView):
    model = Poll
    template_name = 'polllist.html'