from django.urls import path
from .views import home, room_details, create_room

urlpatterns = [
    path("", home, name="home"),
    path("room/<int:pk>/", room_details, name="roomDetails"),
    path("new/room/", create_room, name="create_room"),
]
