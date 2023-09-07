from rest_framework import viewsets, permissions, serializers
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self) -> list:
        if self.action in ["create", "destroy"]:
            return [permissions.IsAdminUser()]
        elif self.action in ["update", "partial_update"]:
            return [permissions.IsAuthenticated()]
        return []

    def get_serializer_class(self) -> serializers:
        if self.action == 'create':
            return CreateUserSerializer
        elif self.action in ["update", "partial_update"]:
            return UpdateUserSerializer
        else:
            return UserSerializer

