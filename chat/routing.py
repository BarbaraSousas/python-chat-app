from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
  path(r'ws/chat/(?P<room_name>\w+)/', ChatConsumer),
]

# custom_routing = [
#   re_path("chat.receive", chat_join, command="^join$"),
#   re_path("chat.receive", chat_leave, command="^leave$"),
#   re_path("chat.receive", chat_send, command="^send$"),
# ]