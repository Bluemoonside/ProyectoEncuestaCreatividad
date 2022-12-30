from django.urls import path, include
from .views import  (Indicators,MeasurementCriterions,Dimensions,
                     MeasurementCriterionListView ,MeasurementCriterionCreateView,
                     MeasurementCriterionUpdateView,MeasurementCriterionDeleteView,
                     IndicatorListView ,IndicatorCreateView,
                     IndicatorUpdateView,IndicatorDeleteView,
                     DimensionListView ,DimensionCreateView,
                     DimensionUpdateView,DimensionDeleteView,)

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
      
      path('listIndicator/gestionDimension/',Dimensions),
     
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
      
      # URL para Dimension
      path('listDimension/', DimensionListView.as_view(),name='listar_dimension'  ),
      path('listDimension/createdDimension/', DimensionCreateView.as_view() ),
      path('listDimension/updateDimension/<pk>', DimensionUpdateView.as_view() ),
      path('listDimension/deleteDimension/<pk>', DimensionDeleteView.as_view() ),
]
