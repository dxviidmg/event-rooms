from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, status
from accounts.permissions import IsBussinesUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

class UserViewSet(viewsets.ModelViewSet):
#    permission_classes = [IsBussinesUser, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
