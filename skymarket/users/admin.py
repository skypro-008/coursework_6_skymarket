from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Просмотр пользователей."""

    list_filter = ("id", "email")
