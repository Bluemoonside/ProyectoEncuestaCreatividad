from django import forms
from Models.models import Poll, Question

#create yours forms
class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = [
            'question',
        ]
        labels = {
            'question': 'Pregunta',
        }
        widgets = {
            'question': forms.SelectMultiple(attrs={'class':'form-control'})
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question_text',
            'type',
            'measurement_criterion'
        ]
        labels = {
            'question_text': 'Texto de la pregunta',
            'type': 'Tipo',
            'measurement_criterion': 'Criterio de Medida',
        }
        widgets = {
            'question_text': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(),
            'measurement_criterion': forms.Select(attrs={'class':'form-control'}),
        }