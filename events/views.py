from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer
from rest_framework import viewsets, status
from accounts.permissions import IsBussinesUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsBussinesUser, IsAuthenticated]
#    queryset = 
    serializer_class = EventSerializer

    def get_queryset(self):
        if self.request.user.get_type_display() == 2:
            return Event.objects.filter(type=1)
        return Event.objects.all()
        
    def create(self, request):
        data = request.data
        events = Event.objects.filter(date=data['date'], room=data['room'])
        if events.exists():
            raise ValidationError("There is an event for this date and room")

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        data = request.data
        event = Event.objects.get(pk=data['event'])
        if event.get_type_display() == 'Private':
            raise ValidationError("This event is private")

        if event.has_places() is False:
            raise ValidationError("This event is full")

        bookings = Booking.objects.filter(**data)
        if bookings.exists():
            raise ValidationError("You have place in this event, you can not book twice")

        
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)