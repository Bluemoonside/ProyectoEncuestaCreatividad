from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models.models import Question
from Poll.Forms.QuestionForm import QuestionForm
from django.urls import reverse_lazy 
from django.views.generic import CreateView


class QuestionCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'createquestion.html'
    success_url = reverse_lazy('createpoll')
    permission_required = 'Models.add_question'
    permission_denied_message = 'Usuario No Autorizado'