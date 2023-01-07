from django.shortcuts import render
from Models.models import Question
from django.urls import reverse_lazy 
from django.views.generic import DeleteView


class QuestionDelete(DeleteView):
    model = Question
    template_name = 'deletequestion.html'
    success_url = reverse_lazy('questionlist')