from rest_framework.permissions import BasePermission
from users.models import UserRoles


class IsAdmin(BasePermission):
    """Проверка наличия прав администратора."""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.role == UserRoles.ADMIN


class IsOwner(BasePermission):
    """Проверка наличия прав создателя."""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user and obj.author == request.user
