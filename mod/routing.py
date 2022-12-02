from django.urls import re_path, path
from . import consumer

websocket_urlpatterns = [
        re_path(r'ws/mod/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
        path('ws/some_url/', consumer.WSConsumer.as_asgi())
 ]
