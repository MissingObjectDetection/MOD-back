from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import mod.routing

application = ProtocolTypeROuter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            mod.routing.websocket_urlpatterns
            )
        ),
})
