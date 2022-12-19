from django.urls import path
from .views import *

urlpatterns = [
    path("", propiedades_inicio, name="propiedades_inicio"),
    path("buscador/", buscador, name="buscador"),
    path("detalles/<str:oferta_enviada>/<int:id>/<str:slug>", propiedades_detalles, name="propiedades_detalle"),
    path("ofertar/<int:id>/<str:slug>", ofertar, name="ofertar"),
]