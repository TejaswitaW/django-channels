from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sc/',consumers.TaskSyncConsumer.as_asgi()),
    path('ws/ac/',consumers.TaskAsyncSyncConsumer.as_asgi()),
]