from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}

class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    ROLE_CHOICES = (
        ('user', 'пользователь'),
        ('admin', 'администратор'),
        ('moderator', 'модератор'),
    )

    first_name = models.CharField(max_length=25, verbose_name='имя')
    last_name = models.CharField(max_length=255, verbose_name='фамилия')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', verbose_name='роль пользователя')
    image = models.ImageField(upload_to='users/', verbose_name='аватар')

    USENAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'