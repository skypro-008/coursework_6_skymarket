# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsAdmin(BasePermission):
    '''
    Доступ к просмотру для авторизированных пользователей с ролью ADMIN.
    Доступ ADMIN-ов ко всем объектам.
    '''

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN


class IsOwner(BasePermission):
    '''
    Доступ к просмотру для авторизированных пользователей с ролью USER.
    Доступ USER-а только к своему объекту (изменять чужие объекты нельзя).
    '''

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
