from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms.room_form import RoomForm

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
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
