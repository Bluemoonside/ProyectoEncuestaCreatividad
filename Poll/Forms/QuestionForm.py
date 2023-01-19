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
    def clean_tittle(self):
        tittle=self.cleaned_data['tittle']
        for c in tittle:
            if c in'`!@#$%^&*()_=+-}{][><\/"1234567890|~':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return tittle 
    def clean_question_text(self):
        question_text=self.cleaned_data['question_text']
        for c in question_text:
            if c in'`!@#$%^&*()_=+-}{][></"\|1234567890~':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return question_text 