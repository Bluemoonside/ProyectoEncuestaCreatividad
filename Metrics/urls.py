from django.urls import path, include
from .views import  MeasurementCriterionListView

urlpatterns = [
      path('listMeasurementCriterion/', MeasurementCriterionListView.as_view(),name='listar_criterio'  ),
     
]
