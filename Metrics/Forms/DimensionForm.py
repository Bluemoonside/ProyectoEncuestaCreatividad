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
    def clean_description(self):
        description=self.cleaned_data['description']
        for c in description:
            if c in'`!@#$%^&*()_=+-}{][></"\|1234567890~':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return description 
    def clean_weigh(self):
        weigh=self.cleaned_data['weigh']
        if weigh <1:
            raise forms.ValidationError('El peso debe ser mayor que 0.') 
        return weigh 