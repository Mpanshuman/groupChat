from django.urls import path
from .views import home, room_details

urlpatterns = [
    path("", home, name="home"),
    path("room/<int:pk>/", room_details, name="roomDetails"),
]
