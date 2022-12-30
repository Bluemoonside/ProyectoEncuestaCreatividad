from django.forms import ModelForm
from Models.models import MeasurementCriterion,Indicator,Dimension,Variable
from django import forms

# formulario para MeasurementCriterion
class MeasurementCriterionForm(ModelForm):
    class Meta:
        model = MeasurementCriterion
        fields = ['description','value','indicator']
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'value': forms.NumberInput(attrs={'class':'form-control'}),
            'indicator':forms.Select(attrs={'class':'form-control'})
        }

# formulario para Indicator
class IndicatorForm(ModelForm):
    class Meta:
        model = Indicator
        fields = ['description', 'weigh', 'scale']
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'weigh': forms.NumberInput(attrs={'class':'form-control'}),
        }

# formulario para Dimension
class DimensionForm(ModelForm):
    class Meta:
        model = Dimension
        fields = ['description', 'indicators','weigh', 'scale']
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'weigh': forms.NumberInput(attrs={'class':'form-control'}),
            'indicators':forms.Select(attrs={'class':'form-control'})
        }