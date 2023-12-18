from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    '''
    Сериализатор модели User.
    Регистрация пользователя.
    '''
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'password']


class CurrentUserSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели User.
    Отображение данных пользователя.
    '''
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'password']
