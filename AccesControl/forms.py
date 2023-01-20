from django.contrib.auth.forms import AuthenticationForm
from .models import UserP

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-contol'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-contol'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
