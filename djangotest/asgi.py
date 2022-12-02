"""
ASGI config for djangotest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
import mod.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotest.settings')

application = ProtocolTypeRouter(
        {
            "http": get_asgi_application(),
            "websocket": 
                AuthMiddlewareStack(URLRouter(mod.routing.websocket_urlpatterns) ),
            }
        )
