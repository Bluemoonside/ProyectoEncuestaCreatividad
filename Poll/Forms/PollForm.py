from django import forms
from Models.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = [
            'name',
            'question',
        ]
        labels = {
            'name': 'Nombre',
            'question': 'Pregunta',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'question': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
    def clean_name(self):
        name=self.cleaned_data['name']
        for c in name:
            if c in'`!@#$%^&*()_=+-}{][></"\|~1234567890':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return name 