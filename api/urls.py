from django.urls import path, include
from .views import prueba

urlpatterns = [
    path('', prueba, name='prueba')
]
