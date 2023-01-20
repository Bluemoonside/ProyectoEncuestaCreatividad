from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = 'login'