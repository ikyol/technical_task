from typing import Any, Dict

from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "name", "registered_at", "is_active"]


class CreateUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.EmailField(required=True)
    name = serializers.CharField(max_length=128)
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    registered_at = serializers.ReadOnlyField()
    is_active = serializers.BooleanField(default=False)

    @staticmethod
    def validate_email(email: str) -> str:
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already exists")
        return email

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UpdateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    name = serializers.CharField(max_length=128, required=False)
    is_active = serializers.BooleanField(required=False)

    def update(self, instance: User, validated_data: Dict[str, Any]) -> User:
        if 'email' in validated_data:
            instance.email = validated_data['email']
        if 'name' in validated_data:
            instance.name = validated_data['name']
        if 'is_active' in validated_data:
            instance.is_active = validated_data['is_active']
        instance.save()
        return instance
