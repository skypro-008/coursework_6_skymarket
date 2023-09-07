from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

users_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
]

