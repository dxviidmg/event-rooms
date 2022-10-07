from .models import Room
from .serializers import RoomSerializer
from rest_framework import viewsets, status
from accounts.permissions import IsBussinesUser
from rest_framework.permissions import IsAuthenticated
from events.models import Event
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


# The business can create a room with M capacity
class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsBussinesUser]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    # The business can delete a room if said room does not have any events.
    def destroy(self, request, pk=None):
        room = self.get_object()
        events = Event.objects.filter(room=room)
        if events.exists():
            raise ValidationError("There are events for room")
        room.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)