from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return 'No. {}'.format(self.pk)