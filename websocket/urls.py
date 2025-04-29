from django.urls import re_path
from .consumer import BasicConsumer

websocket_urlpatterns = [
    re_path(r'ws/', BasicConsumer.as_asgi())
]