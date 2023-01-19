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
    def clean_description(self):
        description=self.cleaned_data['description']
        for c in description:
            if c in'`!@#$%^&*()_=+-}{][></"\|0123456789~':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return description
    def clean_weigh(self):
        weigh=self.cleaned_data['weigh']
        if weigh <1:
            raise forms.ValidationError('El peso debe ser mayor que 0.') 
        return weigh      