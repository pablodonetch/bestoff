from django.urls import path, re_path
from .consumers import *

websocket_urlpatterns = [
	re_path('ws/propiedad/<int:id>/', WSConsumer.as_asgi()),
]