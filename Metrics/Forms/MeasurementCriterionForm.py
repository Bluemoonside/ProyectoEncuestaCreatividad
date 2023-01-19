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
    def clean_description(self):
        description=self.cleaned_data['description']
        for c in description:
            if c in'`!@#$%^&*()_=+-}{][></"\|0123456789~':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return description 
    def clean_value(self):
        value=self.cleaned_data['value']
        if value <1:
            raise forms.ValidationError('El valor debe ser mayor que 0.') 
        return value 