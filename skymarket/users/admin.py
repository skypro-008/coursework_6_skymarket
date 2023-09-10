from django.contrib import admin

# Register your models here.
from .models import User
# TODO Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# TODO Обычно её всегда оформляют, но в текущей задачи делать её не обязательно
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'phone', 'is_active', 'role')