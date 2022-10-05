from django.db import models

class Room(models.Model):
    capacity = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return 'No. {}'.format(self.pk)