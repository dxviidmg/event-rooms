from email.policy import default
from django.db import models
from rooms.models import Room
from accounts.models import User


class Event(models.Model):
    type_choices = ((1, 'Public'), (2, 'Private'))
    name = models.CharField(max_length=30)
    type = models.PositiveSmallIntegerField(choices=type_choices)
    date = models.DateField()
    time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{}'.format(self.name)

    def count_bookings(self):
        return self.bookings.all().count()

    def has_places(self):
        return self.bookings.all().count() < self.room.capacity


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']
