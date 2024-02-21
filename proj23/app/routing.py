from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/jwc/<str:groupname>/',consumers.ChatJsonWebsocketConsumer.as_asgi()),
    path('ws/ajwc/<str:groupname>/',consumers.ChatAsyncJsonWebsocketConsumer.as_asgi())
]