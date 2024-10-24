from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer
from ..models import User


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

