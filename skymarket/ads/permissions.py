from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    """
    Кастомный класс доступа
    """
    def has_permission(self, request, view):
        if request.user.is_anonymous:    # Анонимные пользователи могут просматривать список объявлений
            return view.action == 'list'
        if request.user.is_authenticated:    # Зарегистрированные пользователи могут просматривать список и создавать/редактировать свои объявления и комментарии
            if view.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
                return True
        if request.user.is_superuser:   # Администраторы могут редактировать/удалять все объявления и комментарии
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:    # Анонимные пользователи могут только просматривать объекты
            return view.action == 'retrieve'
        if request.user.is_authenticated:    # Зарегистрированные пользователи могут редактировать/удалять свои объявления и комментарии
            if view.action in ['update', 'partial_update', 'destroy']:
                if request.user.is_superuser:    # Администраторы могут редактировать/удалять все объявления и комментарии
                    return True
                else:
                    return obj.author == request.user
        return False


class CommentsCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:  # Зарегистрированные пользователи могут просматривать список и создавать/редактировать свои объявления и комментарии
            if view.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
                return True
        if request.user.is_superuser:  # Администраторы могут редактировать/удалять все объявления и комментарии
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:  # Зарегистрированные пользователи могут редактировать/удалять свои объявления и комментарии
            if view.action in ['update', 'partial_update', 'destroy']:
                if request.user.is_superuser:  # Администраторы могут редактировать/удалять все объявления и комментарии
                    return True
                else:
                    return obj.author == request.user
        return False