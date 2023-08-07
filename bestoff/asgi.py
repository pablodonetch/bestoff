import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
import bestoff.consumers  # Importa tu Consumer aquí
from channels.sessions import SessionMiddleware  # Importa el middleware de sesión
from bestoff.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')


application = ProtocolTypeRouter({
	'http':get_asgi_application(),
	'websocket': URLRouter(websocket_urlpatterns),
})