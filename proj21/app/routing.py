from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/jwc/',consumers.ChatJsonWebsocketConsumer.as_asgi()),
    path('ws/ajwc/',consumers.ChatAsyncJsonWebsocketConsumer.as_asgi())
]