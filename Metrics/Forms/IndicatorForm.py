from django import forms
from Models.models import Indicator


# formulario para Indicator
class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = ['description','dimensions', 'weigh', 'scale']  
        labels={
            'description':'Descripción',
            'dimensions':'Dimensión a la que pertenece',
            'weigh':'Peso'
        }
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'weigh': forms.NumberInput(attrs={'class':'form-control'}),
            'dimensions':forms.SelectMultiple(attrs={'class':'form-control'}),
        }