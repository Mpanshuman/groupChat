from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms.room_form import RoomForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    # fetch data from url
    topic_name = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(
        Q(topic__name__icontains=topic_name)
        | Q(name__icontains=topic_name)
        | Q(description__icontains=topic_name)
    )

    # get all the topics
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "topics": topics, "room_count": room_count}
    return render(request, "base/home.html", context)


def room_details(request, pk):
    try:
        room = Room.objects.get(pk=int(pk))
    except Exception as e:
        return render(request, "base/room_details.html", {"error": f"{e}"})
    return render(request, "base/room_details.html", {"room": room})


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "base/room_form.html", {"form": form})


def update_room(request, pk):
    try:
        room = Room.objects.get(pk=int(pk))
    except Exception as e:
        return HttpResponse(f"{e}")
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "base/room_form.html", {"form": form})


def delete_room(request, pk):
    try:
        room = Room.objects.get(pk=int(pk))
    except Exception as e:
        return HttpResponse(f"{e}")
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete_room.html", {"room": room})


def login_user(request):
    context = {"page": "login"}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse(f"user with username {username} does not exist")

        user = authenticate(request, username=username, password=password)

        print(f"authenticated user :{user}")

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Wrong Credentials")
    return render(request, "base/login_register_form.html", context)


def logout_url(request):
    logout(request)
    return redirect("home")


def user_registration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occured during registration")
    return render(request, "base/login_register_form.html", {"form": form})
