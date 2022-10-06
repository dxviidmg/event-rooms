from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

#    def validate(self, data):
#        if self._args != ():
#            return data
#        events = Event.objects.filter(date=data['date'], room=data['room'])
#        if events.exists():
#            raise serializers.ValidationError("There is an event for this date and room")
#        return data
        