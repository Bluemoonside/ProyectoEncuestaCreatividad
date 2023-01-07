from django import forms
from Models.models import MeasurementCriterion


# formulario para MeasurementCriterion
class MeasurementCriterionForm(forms.ModelForm):
    class Meta:
        model = MeasurementCriterion
        fields = ['description','value','indicator']
        
        labels={
            'description':'Descripción',
            'indicator':'Indicador al que pertenece',
            'value':'Valor'
        }
        
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'value': forms.NumberInput(attrs={'class':'form-control'}),
            'indicator':forms.Select(attrs={'class':'form-control'})
        }