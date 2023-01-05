from django import forms
from Models.models import MeasurementCriterion,Indicator,Dimension,Variable,Scale

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


# formulario para Scale
class ScaleForm(forms.ModelForm):
	class Meta:
		model = Scale
		fields =[
			'description',
			'name',
			'max_value',
			'min_value',
			'interval',
		]
		labels = {
			'description': 'Description',
			'name': 'Nombre',
			'max_value': 'Valor Máximo',
			'min_value': 'Valor Mínimo',
			'interval': 'Intervalo',
		} 
		widgets = {
			'description': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'max_value': forms.NumberInput(),
			'min_value': forms.NumberInput(),
			'interval': forms.NumberInput(),    
		}
        
