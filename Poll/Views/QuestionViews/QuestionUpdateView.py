from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models.models import Question
from Poll.Forms.QuestionForm import QuestionForm
from django.urls import reverse_lazy 
from django.views.generic import UpdateView


class QuestionUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'updatequestion.html'
    success_url = reverse_lazy('questionlist')
    permission_required = 'Models.change_question'
    permission_denied_message = 'Usuario No Autorizado'