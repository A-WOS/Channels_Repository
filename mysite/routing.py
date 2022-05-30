import django.urls
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

# from channels.routing import ProtocolTypeRouter
#
# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
# })
