import os

from channels.routing import ProtocolTypeRouter,URLRouter

import app.routing

from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj4.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            app.routing.websocket_urlpatterns
    ))
})
