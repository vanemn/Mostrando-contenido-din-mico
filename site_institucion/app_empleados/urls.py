from django.urls import path
from .views import lista_empleados

urlpatterns = [
    path('', lista_empleados, name= 'lista_empleados'),
]