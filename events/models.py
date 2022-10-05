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
    users = models.ManyToManyField(User)

    def __str__(self) -> str:
        return '{}'.format(self.name)