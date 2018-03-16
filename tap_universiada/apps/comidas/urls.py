from django.urls import path

from .views.index import index
from .views.codigos import codigos
from .views.tablas import tablas

urlpatterns = [
    path('', index),
    path('codigos', codigos),
    path('tablas', tablas)
]
