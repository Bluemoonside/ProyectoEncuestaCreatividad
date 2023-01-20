from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models.models import Question
from django.views.generic import ListView


class QuestionList(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Question
    template_name = 'questionlist.html'
    permission_required = 'Models.view_question'
    permission_denied_message = 'Usuario No Autorizado'