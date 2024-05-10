from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

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
