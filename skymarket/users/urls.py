from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from .apps import UsersConfig

# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

app_name = UsersConfig.name

users_router = SimpleRouter()
users_router.register('', UserViewSet, basename='users')

urlpatterns = [
    path('', include(users_router.urls)),
]
