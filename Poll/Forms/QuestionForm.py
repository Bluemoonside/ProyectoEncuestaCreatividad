from django import forms
from Models.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'tittle',
            'question_text',
            'type',
            'measurement_criterion'
        ]
        labels = {
            'tittle': 'Titulo',
            'question_text': 'Texto de la pregunta',
            'type': 'Tipo',
            'measurement_criterion': 'Criterio de Medida',
        }
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control'}),
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(),
            'measurement_criterion': forms.Select(attrs={'class': 'form-control'}),
        }