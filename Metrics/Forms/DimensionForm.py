from django import forms
from Models.models import Dimension


# formulario para Dimension
class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimension
        fields = ['description', 'variables','weigh', 'scale']
        labels={
            'description':'Descripción',
            'variables':'Variables a la s que pertenece',
            'weigh':'Peso'
        }
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'weigh': forms.NumberInput(attrs={'class':'form-control'}),
            'variables':forms.SelectMultiple(attrs={'class':'form-control'}),
        }