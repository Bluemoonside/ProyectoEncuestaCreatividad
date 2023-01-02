from django.urls import path, include
from .Views.DimensionViews.DimensionDeleteView import *
from .Views.DimensionViews.DimensionListView import *
from .Views.DimensionViews.DimensionUpdateView import *
from .Views.DimensionViews.DimensionCreateViews import *
from .Views.IndicatorsViews.IndicatorCreateView import *
from .Views.IndicatorsViews.IndicatorDeleteView import *
from .Views.IndicatorsViews.IndicatorListView import *
from .Views.IndicatorsViews.IndicatorUpdateView import *
from .Views.MeasurementCriterionViews.MeasurementCriterionCreateView import *
from .Views.MeasurementCriterionViews.MeasurementCriterionDeleteView import *
from .Views.MeasurementCriterionViews.MeasurementCriterionListViews import *
from .Views.MeasurementCriterionViews.MeasurementCriterionUpdateView import *
from .Views.ScaleViews.ScaleCreateView import *
from .Views.ScaleViews.ScaleDeleteView import *
from .Views.ScaleViews.ScaleListView import *
from .Views.ScaleViews.ScaleUpdateView import *
from .Views.VariableViews.VariableCreateView import *
from .Views.VariableViews.VariableDeleteView import *
from .Views.VariableViews.VariableListView import *
from .Views.VariableViews.VariableUpdateView import *

urlpatterns = [
      #URL para hacer funcionar el narbar
      path('measurementcriterions/measurementcriterions/', MeasurementCriterions),     
      path('indicators/measurementcriterions/', MeasurementCriterions),
      path('indicators/created/measurementcriterions/', MeasurementCriterions  ),
      path('indicators/update/measurementcriterions/', MeasurementCriterions  ),
      path('indicators/delete/measurementcriterions/', MeasurementCriterions  ),
      path('dimensions/measurementcriterions/', MeasurementCriterions),
      path('dimensions/created/measurementcriterions/', MeasurementCriterions  ),
      path('dimensions/update/measurementcriterions/', MeasurementCriterions  ),
      path('dimensions/delete/measurementcriterions/', MeasurementCriterions  ),
      path('variables/measurementcriterions/', MeasurementCriterions),
      path('variables/created/measurementcriterions/', MeasurementCriterions  ),
      path('variables/update/measurementcriterions/', MeasurementCriterions  ),
      path('variables/delete/measurementcriterions/', MeasurementCriterions  ),
      
      path('indicators/indicators/',Indicators ),
      path('measurementcriterions/indicators/',Indicators ),
      path('measurementcriterions/update/indicators/', Indicators  ),
      path('measurementcriterions/created/indicators/', Indicators  ),
      path('measurementcriterions/delete/indicators/', Indicators  ),
      path('dimensions/indicators/',Indicators ),
      path('dimensions/update/indicators/', Indicators  ),
      path('dimensions/created/indicators/', Indicators  ),
      path('dimensions/delete/indicators/', Indicators  ),
      path('variables/indicators/',Indicators ),
      path('variables/update/indicators/', Indicators  ),
      path('variables/created/indicators/', Indicators  ),
      path('variables/delete/indicators/', Indicators  ),
      
      path('dimensions/dimensions/',Dimensions),
      path('indicators/dimensions/', Dimensions),
      path('indicators/created/dimensions/', Dimensions  ),
      path('indicators/update/dimensions/', Dimensions  ),
      path('indicators/delete/dimensions/', Dimensions  ),
      path('measurementcriterions/dimensions/', Dimensions),
      path('measurementcriterions/created/dimensions/', Dimensions  ),
      path('measurementcriterions/update/dimensions/', Dimensions  ),
      path('measurementcriterions/delete/dimensions/', Dimensions  ),
      path('variables/dimensions/', Dimensions),
      path('variables/created/dimensions/', Dimensions  ),
      path('variables/update/dimensions/', Dimensions  ),
      path('variables/delete/dimensions/', Dimensions  ), 
      
      path('variables/variables/',Variables),
      path('indicators/variables/', Variables),
      path('indicators/created/variables/', Variables ),
      path('indicators/update/variables/', Variables ),
      path('indicators/delete/variables/', Variables ),
      path('measurementcriterions/variables/', Variables),
      path('measurementcriterions/created/variables/', Variables ),
      path('measurementcriterions/update/variables/', Variables ),
      path('measurementcriterions/delete/variables/', Variables ), 
      path('dimensions/variables/', Variables),
      path('dimensions/update/variables/', Variables ),
      path('dimensions/created/variables/', Variables ), 
      path('dimensions/delete/variables/', Variables ),

     
     # URL para MeasurementCriterion
      path('measurementcriterions/', MeasurementCriterionListView.as_view(),name='listar_criterio'  ),
      path('measurementcriterions/created/', MeasurementCriterionCreateView.as_view() ),
      path('measurementcriterions/update/<pk>', MeasurementCriterionUpdateView.as_view() ),
      path('measurementcriterions/delete/<pk>', MeasurementCriterionDeleteView.as_view() ),
      
       # URL para Indicator
      path('indicators/', IndicatorListView.as_view(),name='listar_indicator'  ),
      path('indicators/created/', IndicatorCreateView.as_view() ),
      path('indicators/update/<pk>', IndicatorUpdateView.as_view() ),
      path('indicators/delete/<pk>', IndicatorDeleteView.as_view() ),

      # URL para Dimension
      path('dimensions/', DimensionListView.as_view(),name='listar_dimension'  ),
      path('dimensions/created/', DimensionCreateView.as_view() ),
      path('dimensions/update/<pk>', DimensionUpdateView.as_view() ),
      path('dimensions/delete/<pk>', DimensionDeleteView.as_view() ),
      
        # URL para Variable
      path('variables/', VariableListView.as_view(),name='listar_variable'  ),
      path('variables/created/', VariableCreateView.as_view() ),
      path('variables/update/<pk>', VariableUpdateView.as_view() ),
      path('variables/delete/<pk>', VariableDeleteView.as_view() ),
      
      #URls para Scala
      path('scales/', ScaleListView.as_view(),name='listar_scale'  ),
      path('scales/create/', ScaleCreateView.as_view() ),
      path('scales/update/<pk>', ScaleUpdateView.as_view() ),
      path('scales/delete/<pk>', ScaleDeleteView.as_view() ),
]
