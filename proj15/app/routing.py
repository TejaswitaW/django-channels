from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/swc/',consumers.SyncWebsocketConsumer.as_asgi()),
    path('ws/aswc/',consumers.AsyncWebsocketConsumer.as_asgi())
]