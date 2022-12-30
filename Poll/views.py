from django.shortcuts import render
from Models.models import *
from .forms import *
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
class PollList(ListView):
    model = Poll
    template_name = 'polllist.html'

class PollCreate(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'createpoll.html'
    success_url = reverse_lazy('polllist')

class PollUpdate(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'createpoll.html'
    success_url = reverse_lazy('polllist')

class PollDelete(DeleteView):
    model = Poll
    template_name = 'deletepoll.html'
    success_url = reverse_lazy('polllist')

class QuestionList(ListView):
    model = Question
    template_name = 'questionlist.html'

class QuestionCreate(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'createquestion.html'
    success_url = reverse_lazy('createpoll')

class QuestionUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'createquestion.html'
    success_url = reverse_lazy('createpoll')

class QuestionDelete(DeleteView):
    model = Question
    template_name = 'deletequestion.html'
    success_url = reverse_lazy('questionlist')