from django.urls import path
from .views import websocket_demo

urlpatterns = [
    path('users/websocket/', websocket_demo, name='websocket_demo'),
]
