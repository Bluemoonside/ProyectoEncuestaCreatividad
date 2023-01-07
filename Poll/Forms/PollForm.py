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