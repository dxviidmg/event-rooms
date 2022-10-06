from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer
from rest_framework import viewsets, status
from accounts.permissions import IsBussinesUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import permissions


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [IsAuthenticated()]
        # The business can create events for every room.
        return [IsBussinesUser(), IsAuthenticated()]

    def get_queryset(self):
        if self.request.user.get_type_display() == 'Customer':
            # A customer can see all the available public events.
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


# A customer can book a place for an event.
# A customer can cancel its booking for an event.
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request):
        data = request.data
        event = Event.objects.get(pk=data['event'])

        # If the event is public, any customer can book a space.
        # If the event is private, no one else can book a space in the room.
        if event.get_type_display() == 'Private':
            raise ValidationError("This event is private")

        # A customer can book a space for an event, if the event is public and there is still space available.
        # A customer can cancel its booking and their space should be available again.
        if event.has_places() is False:
            raise ValidationError("This event is full")

        bookings = Booking.objects.filter(**data)
        if bookings.exists():
            # A customer cannot book a space twice for the same event.
            raise ValidationError("You have place in this event, you can not book twice")

        
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)







