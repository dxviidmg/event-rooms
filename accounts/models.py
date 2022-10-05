from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    type_choices = (
        (1, 'Bussines'),
        (2, 'Customer'),

    )
    type = models.IntegerField(null=True, choices=type_choices)