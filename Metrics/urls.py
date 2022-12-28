from django.urls import path, include
from .views import MeasurementCriterionCreateView ,MeasurementCriterionListView

urlpatterns = [
      path('listarMeasurementCriterion/', MeasurementCriterionListView.as_view(),name='listar_criterio'  ),
]
