from django.contrib.auth.views import logout_then_login
from django.urls import path
from django.conf.urls import handler404, handler500, handler403
from .views import Login, Error403, Error404, Error500

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),
]

handler404 = Error404.as_view()
handler403 = Error403.as_view()
handler500 = Error500.as_error_view()