from django.urls import path, re_path
from bestoff.consumers import WSConsumer

websocket_urlpatterns = [
	re_path('ws/propiedad/(?P<propiedad_id>\d+)', WSConsumer.as_asgi()),
]
