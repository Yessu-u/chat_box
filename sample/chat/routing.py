from django.urls import path, re_path

from . import users

websocket_urlpatters = [
    re_path('/groups/<str:room_name>/',users.ChatConsumer.as_asgi()),
]