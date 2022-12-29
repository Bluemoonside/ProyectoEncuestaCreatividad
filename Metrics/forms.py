from django.forms import ModelForm
from Models.models.MeasurementCriterion import MeasurementCriterion

# formulario para MeasurementCriterion
class MeasurementCriterionForm(ModelForm):
    class Meta:
        model = MeasurementCriterion
        fields = ['description','value','indicator']
