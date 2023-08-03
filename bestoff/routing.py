from django.urls import path, re_path
from .consumers import WSConsumer



ws_urlpatterns = [
	re_path('ws/some_url', WSConsumer.as_asgi())
]