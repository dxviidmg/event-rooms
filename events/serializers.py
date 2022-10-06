from rest_framework import serializers
from .models import Event, Booking


class EventSerializer(serializers.ModelSerializer):
    type_display = serializers.SerializerMethodField()
    count_bookings = serializers.SerializerMethodField()
    has_places = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_type_display(self, obj):
        return obj.get_type_display()

    def get_count_bookings(self, obj):
        return obj.count_bookings()

    def get_has_places(self, obj):
        return obj.has_places()


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'