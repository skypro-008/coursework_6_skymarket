from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import BaseUserManager

NULLABLE = {'null': True, 'blank': True}


class UserManager(BaseUserManager):
    """
    функция создания пользователя — в нее мы передаем обязательные поля
    """

    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role="user"
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role="admin"
        )

        user.save(using=self._db)
        return user


class UserRole:
    choices = (
        ('users', 'юзер'),
        ('admin', 'админ')
    )


class User(AbstractBaseUser):
    username = None

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    email = models.EmailField(max_length=150, verbose_name='электронная почта', unique=True)
    password = models.CharField(max_length=100, verbose_name='пароль')
    phone = models.CharField(max_length=50, unique=True, verbose_name='номер телефона')
    image = models.ImageField(upload_to='user', null=True, blank=True, verbose_name='аватар')
    role = models.CharField(max_length=10, choices=UserRole.choices, default=UserRole.choices[0])

    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()
