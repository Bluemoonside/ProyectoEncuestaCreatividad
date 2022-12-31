from django.urls import path, include
from .views import *

urlpatterns = [
      #URL ara direccionar a las difrerntes grstiones de tablas
      path('measurementcriterions/measurementcriterions/', MeasurementCriterions),     
      path('indicators/measurementcriterions/', MeasurementCriterions),
      path('indicators/created/measurementcriterions/', MeasurementCriterions  ),
      path('indicators/update/measurementcriterions/', MeasurementCriterions  ),
      path('indicators/delete/measurementcriterions/', MeasurementCriterions  ),
      path('dimensions/measurementcriterions/', MeasurementCriterions),
      path('dimensions/created/measurementcriterions/', MeasurementCriterions  ),
      path('dimensions/update/measurementcriterions/', MeasurementCriterions  ),
      path('dimensions/delete/measurementcriterions/', MeasurementCriterions  ),
      
      path('indicators/indicators/',Indicators ),
      path('measurementcriterions/indicators/',Indicators ),
      path('measurementcriterions/update/indicators/', Indicators  ),
      path('measurementcriterions/created/indicators/', Indicators  ),
      path('measurementcriterions/delete/indicators/', Indicators  ),
      path('dimensions/indicators/',Indicators ),
      path('dimensions/update/indicators/', Indicators  ),
      path('dimensions/created/indicators/', Indicators  ),
      path('dimensions/delete/indicators/', Indicators  ),
      
      path('dimensions/dimensions/',Dimensions),
      path('indicators/dimensions/', Dimensions),
      path('indicators/created/dimensions/', Dimensions  ),
      path('indicators/update/dimensions/', Dimensions  ),
      path('indicators/delete/dimensions/', Dimensions  ),
      path('measurementcriterions/dimensions/', Dimensions),
      path('measurementcriterions/created/dimensions/', Dimensions  ),
      path('measurementcriterions/update/dimensions/', Dimensions  ),
      path('measurementcriterions/delete/dimensions/', Dimensions  ), 
     
      path('measurementcriterions/', MeasurementCriterionListView.as_view(),name='listar_criterio'  ),
      path('measurementcriterions/created/', MeasurementCriterionCreateView.as_view() ),
      path('measurementcriterions/update/<pk>', MeasurementCriterionUpdateView.as_view() ),
      path('measurementcriterions/delete/<pk>', MeasurementCriterionDeleteView.as_view() ),
      
      path('scale/list/', ScaleListView.as_view(),name='listar_scale'  ),
      path('scale/list/scale/create/', ScaleCreateView.as_view() ),
      path('scale/list/scale/update/<pk>', ScaleUpdateView.as_view() ),
      path('scale/list/scale/delete/<pk>', ScaleDeleteView.as_view() ),
]
