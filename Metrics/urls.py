from django.urls import path, include
from .views import *

urlpatterns = [
      #URL ara direccionar a las difrerntes grstiones de tablas
      path('listIndicator/gestionMeasurementCriterion/', MeasurementCriterions),
      path('listMeasurementCriterion/gestionMeasurementCriterion/', MeasurementCriterions),
      path('listIndicator/createdIndicator/gestionMeasurementCriterion/', MeasurementCriterions  ),
      path('listIndicator/updateIndicator/gestionMeasurementCriterion/', MeasurementCriterions  ),
      path('listIndicator/deleteIndicator/gestionMeasurementCriterion/', MeasurementCriterions  ),
      
      path('listMeasurementCriterion/gestionIndicator/',Indicators ),
      path('listIndicator/gestionIndicator/',Indicators ),
      path('listMeasurementCriterion/updateMeasurementCriterion/gestionIndicator/', Indicators  ),
      path('listMeasurementCriterion/createdMeasurementCriterion/gestionIndicator/', Indicators  ),
      path('listMeasurementCriterion/deleteMeasurementCriterion/gestionIndicator/', Indicators  ),
      # URL para MeasurementCriterion
      path('listMeasurementCriterion/', MeasurementCriterionListView.as_view(),name='listar_criterio'  ),
      path('listMeasurementCriterion/createdMeasurementCriterion/', MeasurementCriterionCreateView.as_view() ),
      path('listMeasurementCriterion/updateMeasurementCriterion/<pk>', MeasurementCriterionUpdateView.as_view() ),
      path('listMeasurementCriterion/deleteMeasurementCriterion/<pk>', MeasurementCriterionDeleteView.as_view() ),
      # URL para Indicator
      path('listIndicator/', IndicatorListView.as_view(),name='listar_indicator'  ),
      path('listIndicator/createdIndicator/', IndicatorCreateView.as_view() ),
      path('listIndicator/updateIndicator/<pk>', IndicatorUpdateView.as_view() ),
      path('listIndicator/deleteIndicator/<pk>', IndicatorDeleteView.as_view() ), 
      # URL para Scale
      path('listscale/', ScaleListView.as_view(),name='listar_scale'  ),
      path('listscale/createdscale/', ScaleCreateView.as_view() ),
      path('listscale/updatescale/<pk>', ScaleUpdateView.as_view() ),
      path('listscale/deletescale/<pk>', ScaleDeleteView.as_view() ), 
]
