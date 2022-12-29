from django.urls import path, include
from .views import  MeasurementCriterionListView ,MeasurementCriterionCreateView,MeasurementCriterionUpdateView,MeasurementCriterionDeleteView

urlpatterns = [
      path('listMeasurementCriterion/', MeasurementCriterionListView.as_view(),name='listar_criterio'  ),
      path('listMeasurementCriterion/createdMeasurementCriterion/', MeasurementCriterionCreateView.as_view() ),
      path('listMeasurementCriterion/updateMeasurementCriterion/<pk>', MeasurementCriterionUpdateView.as_view() ),
      path('listMeasurementCriterion/deleteMeasurementCriterion/<pk>', MeasurementCriterionDeleteView.as_view() ),
]
