from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
  path('chat/', ChatConsumer),
]

# custom_routing = [
#   re_path("chat.receive", chat_join, command="^join$"),
#   re_path("chat.receive", chat_leave, command="^leave$"),
#   re_path("chat.receive", chat_send, command="^send$"),
# ]