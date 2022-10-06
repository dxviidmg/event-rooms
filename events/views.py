from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets, status
from accounts.permissions import IsBussinesUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsBussinesUser, IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    
    def create(self, request):
        data = request.data 
        events = Event.objects.filter(date=data['date'], room=data['room'])
        if events.exists():
            raise ValidationError("There is an event for this date and room")

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)