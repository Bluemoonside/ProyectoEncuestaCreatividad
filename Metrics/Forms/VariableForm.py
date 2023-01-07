from django import forms
from Models.models import Variable


# formulario para Variable
class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = ['description','name', 'scale']
        labels={
            'description':'Descripción',
            'name':'Nombre'
        } 
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }