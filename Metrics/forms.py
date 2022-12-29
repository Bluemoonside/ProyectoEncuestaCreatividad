from django.forms import ModelForm
from Models.models import MeasurementCriterion,Indicator,Dimension,Variable

# formulario para MeasurementCriterion
class MeasurementCriterionForm(ModelForm):
    class Meta:
        model = MeasurementCriterion
        fields = ['description','value','indicator']
