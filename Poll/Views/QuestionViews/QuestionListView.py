from django.shortcuts import render
from Models.models import Question
from django.views.generic import ListView


class QuestionList(ListView):
    model = Question
    template_name = 'questionlist.html'