import os
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from bestoff.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestoff.settings')

application=ProtocolTypeRouter({
	'http':get_asgi_application(),
	'websocket': URLRouter(websocket_urlpatterns),
	})