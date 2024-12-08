from django.contrib.auth import get_user_model
from djoser.serializers import \
    UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """Сериализатор для регистрации пользователя."""

    class Meta:
        model = User
        fields = "__all__"


class CurrentUserSerializer(serializers.ModelSerializer):
    """Сериализатор текущего пользователя."""

    class Meta:
        model = User
        fields = "__all__"
