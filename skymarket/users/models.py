from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# Constants
NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    # TODO закончите enum-класс для пользователя
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone = PhoneNumberField(max_length=100, verbose_name='Номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    image = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
