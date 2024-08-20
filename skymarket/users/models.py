from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserManager


class UserRoles:
    """Модель выбора роли пользователя."""
    ADMIN = "admin"
    USER = "user"
    choices = [("admin", "Администратор"), ("user", "Пользователь")]


class User(AbstractBaseUser):
    """Модель пользователя."""
    username = None
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = PhoneNumberField(verbose_name="Телефон")
    role = models.CharField(
        max_length=10, choices=UserRoles.choices, verbose_name="Роль", default=UserRoles.USER
    )
    image = models.ImageField(
        upload_to="users", verbose_name="Аватар", null=True, blank=True
    )
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone", "role", "image"]

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

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
