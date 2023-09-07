from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
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

    first_name = models.CharField(max_length=25, verbose_name='имя', **NULLABLE)
    last_name = models.CharField(max_length=255, verbose_name='фамилия', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', verbose_name='роль пользователя')
    image = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # менеджер объектов
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'