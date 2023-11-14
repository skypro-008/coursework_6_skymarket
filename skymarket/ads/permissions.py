# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsAdmin(BasePermission):
    '''Доступ только для авторизированных пользователей с ролью ADMIN'''

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN


class IsOwner(BasePermission):
    '''Достип авторизированного пользователя к своему объявлению'''

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
