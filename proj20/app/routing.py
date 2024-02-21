from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/swc/<str:groupname>/',consumers.SyncWebsocketConsumer.as_asgi()),
    path('ws/aswc/<str:groupname>/',consumers.AsyncWebsocketConsumer.as_asgi())
]