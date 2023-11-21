from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
# TODO Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# TODO Обычно её всегда оформляют, но в текущей задачи делать её не обязательно


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''
    Пользователи - отображение в админ-панели Jango.
    Фильтрует по роли пользователя.
    '''
    list_display = ('email', 'first_name', 'phone', 'is_active', 'role', 'pk')
    list_filter = ('role',)
