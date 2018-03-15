from django.urls import path

from .views.index import index
from .views.codigos import codigos

urlpatterns = [
    path('', index),
    path('codigos', codigos)
]
