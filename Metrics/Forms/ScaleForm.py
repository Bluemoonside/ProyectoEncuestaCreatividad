from django import forms
from Models.models import Scale


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