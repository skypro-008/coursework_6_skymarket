from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserManager, UserRole

NULLABLE = {'null': True, 'blank': True}


class User(AbstractBaseUser):
    username = None

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    email = models.EmailField(max_length=150, verbose_name='электронная почта', unique=True)
    password = models.CharField(max_length=100, verbose_name='пароль')
    phone = models.CharField(max_length=50, unique=True, verbose_name='номер телефона')
    image = models.ImageField(upload_to='user', null=True, blank=True, verbose_name='аватар')
    role = models.CharField(max_length=30, choices=UserRole.choices, default=UserRole.USER, verbose_name='Роль')
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
