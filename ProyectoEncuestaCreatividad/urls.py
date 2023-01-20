"""ProyectoEncuestaCreatividad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403
from AccesControl.views import Error403, Error404, Error500
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/', include('AccesControl.urls'), name='accounts'),
    path('admin/', admin.site.urls),
    path('models/', include('Models.urls')),
    path('metrics/', include('Metrics.urls')),
    path('poll/', include('Poll.urls')),
]

handler404 = Error404.as_view()
handler403 = Error403.as_view()
handler500 = Error500.as_error_view()