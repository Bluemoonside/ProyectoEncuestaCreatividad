from django.forms import ModelForm
from Models.models import MeasurementCriterion,Indicator,Dimension,Variable

# formulario para MeasurementCriterion
class MeasurementCriterionForm(ModelForm):
    class Meta:
        model = MeasurementCriterion
        fields = ['description','value','indicator']

# formulario para Indicator
class IndicatorForm(ModelForm):
    class Meta:
        model = Indicator
        fields = ['description', 'weigh', 'scale']

# formulario para Dimension
class DimensionForm(ModelForm):
    class Meta:
        model = Dimension
        fields = ['description', 'indicators','weigh', 'scale']