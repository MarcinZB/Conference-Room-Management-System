from django.shortcuts import render, redirect
from django.views import View
from .models import ConferenceRoom, RoomReservation
import datetime


# Create your views here.

class AddRoomView(View):
    def get(self, request):
        return render(request, "add_room.html")

    def post(self, request):
        name = request.POST.get("room-name")
        capacity = request.POST.get("capacity")
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("projector") == "on"

        if not name:
            return render(request, "add_room.html", context={"error": "Nie podano nazwy sali"})
        if capacity <= 0:
            return render(request, "add_room.html", context={"error": "Pojemność musi być dodatnia"})
        if ConferenceRoom.objects.filter(name=name).first():
            return render(request, "add_room.html", context={"error": "Sala o podanej nazwie istnieje"})

        ConferenceRoom.objects.create(name=name, capacity=capacity, projector_availability=projector)
        return redirect("room-list")

class RoomListView(View):
    def get(self, request):
        rooms = ConferenceRoom.objects.all()
        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.roomreservation_set.all()]
            room.reserverd = datetime.date.today() in reservation_dates
        return render(request, "rooms.html", context={"rooms": rooms})


class DeleteRoomView(View):
    def get(self,request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        room.delete()
        return redirect("room-list")


class ModifyRoomView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        return render(request, "modify_room.html", context={"room": room})

    def post(self,request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        name = request.POST.get("room-name")
        capacity = request.POST.get("capacity")
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("projector") == "on"

        if not name:
            return render(request,"modify_room.html", context={"room":room, "error": "Nie podano nazwy sali"})
        if capacity <= 0:
            return render(request, "modify_room.html", context={"room": room, "error": "Pojemność sali musi być dodatnia"})

        if name != room.name and ConferenceRoom.objects.filter(name=name).first():
            return render(request, "modify_room.html", context={"room": room, "error": "Sala o podanej nazwie istnieje"})

        room.name = name
        room.capacity = capacity
        room.projector_availability = projector
        room.save()
        return redirect("room-list")

class ReservationView(View):
    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        return render(request, 'reservation.html', context={"room": room})

    def post(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        date = request.POST.get("reservation-date")
        comment = request.POST.get("comment")

        if RoomReservation.objects.filter(room_id=room, date=date):
            return render(request, "reservation.html", context={"room": room, "error": "Sala jest już zarezerwowana"})
        if date < str(datetime.date.today()):
            return render(request, "reservation.html", context={"room": room, "error": "Data jest z przeszłości"})
        RoomReservation.objects.create(room_id=room, date=date, comment=comment)
        return redirect("room-list")

class RoomDetailsView(View):
    def get(self,request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        reservations = room.roomreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, "room_details.html", context={"room": room, "reservations": reservations})

class SearchView(View):
    def get(self,request):
        name = request.GET.get("room-name")
        capacity = request.GET.get("capacity")
        capacity = int(capacity) if capacity else 0
        projector = request.GET.get("projector") == "on"

        rooms = ConferenceRoom.objects.all()

        if projector:
            rooms = rooms.filter(projector_availability=projector)
        if capacity:
            rooms = rooms.filter(capacity__gte=capacity)
        if name:
            rooms.filter(name__contains=name)

        for room in rooms:
            reservation_dates = [reservation.date for reservation in room.roomreservation_set.all()]
            room.reserved = str(datetime.date.today()) in reservation_dates

        return render(request, "rooms.html", context={"rooms": rooms, "date": datetime.date.today()})