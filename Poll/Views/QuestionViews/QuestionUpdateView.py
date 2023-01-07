from django.shortcuts import render
from Models.models import Question
from Poll.Forms.QuestionForm import QuestionForm
from django.urls import reverse_lazy 
from django.views.generic import UpdateView


class QuestionUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'updatequestion.html'
    success_url = reverse_lazy('questionlist')