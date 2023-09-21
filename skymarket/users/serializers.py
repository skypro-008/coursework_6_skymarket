from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
    Сериализатор для регистрации пользователя
    """
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "phone"]


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    Сериализация данных пользователя
    """
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone"]
