import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from ejemplo.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestoff.settings')

application=ProtocolTypeRouter({
	'http':get_asgi_application(),
	'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))
	})