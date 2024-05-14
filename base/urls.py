from django.urls import path
from .views import (
    home,
    room_details,
    create_room,
    update_room,
    delete_room,
    login_user,
    logout_url,
    user_registration,
)

urlpatterns = [
    path("", home, name="home"),
    path("room/<int:pk>/", room_details, name="roomDetails"),
    path("new/room/", create_room, name="create_room"),
    path("room/edit/<int:pk>/", update_room, name="update_room"),
    path("room/delete/<int:pk>/", delete_room, name="delete_room"),
    path("login/", login_user, name="loginuser"),
    path("register/", user_registration, name="registeruser"),
    path("logout/", logout_url, name="logout"),
]
