# mysite/asgi.py
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

import notify.routing

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": 
        AuthMiddlewareStack(
            URLRouter(
                notify.routing.websocket_urlpatterns
            )
            ),
})