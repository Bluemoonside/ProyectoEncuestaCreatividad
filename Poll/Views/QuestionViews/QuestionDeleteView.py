from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from Models.models import Question
from django.urls import reverse_lazy 
from django.views.generic import DeleteView


class QuestionDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    model = Question
    template_name = 'deletequestion.html'
    success_url = reverse_lazy('questionlist')
    permission_required = 'Models.delete_question'
    permission_denied_message = 'Usuario No Autorizado'