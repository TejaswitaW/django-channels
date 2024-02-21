from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:groupname>/',consumers.TaskSyncConsumer.as_asgi()),
    path('ws/ac/<str:groupname>/',consumers.TaskAsyncSyncConsumer.as_asgi()),
]