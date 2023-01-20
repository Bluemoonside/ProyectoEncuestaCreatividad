from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from .forms import FormularioLogin

class Login(LoginView):
    template_name = 'Login/login.html'
    form_class = FormularioLogin

class Error404(TemplateView):
    template_name = 'error_404.html'

class Error500(TemplateView):
    template_name = 'error_500.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view

class Error403(TemplateView):
    template_name = 'error_403.html'