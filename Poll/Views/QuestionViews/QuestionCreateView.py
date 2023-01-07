from django.shortcuts import render
from Models.models import Question
from Poll.Forms.QuestionForm import QuestionForm
from django.urls import reverse_lazy 
from django.views.generic import CreateView


class QuestionCreate(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'createquestion.html'
    success_url = reverse_lazy('createpoll')