from django.urls import path
from .views import *

urlpatterns = [
    path("", propiedades_inicio, name="propiedades_inicio"),
    path("santiago/", santiago, name="santiago"),
    path("valparaiso/", valparaiso, name="valparaiso"),
    path("concepcion/", concepcion, name="concepcion"),
    path("buscador/", buscador, name="buscador"),
    path("detalles/<int:id>/<str:slug>", propiedades_detalles, name="propiedades_detalle"),
]