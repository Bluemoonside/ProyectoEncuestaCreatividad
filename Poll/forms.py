from django import forms
from Models.models import Poll, Question

#create yours forms
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
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'question': forms.SelectMultiple(attrs={'class':'form-control'})
        }

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
            'tittle': forms.TextInput(attrs={'class':'form-control'}),
            'question_text': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(),
            'measurement_criterion': forms.Select(attrs={'class':'form-control'}),
        }