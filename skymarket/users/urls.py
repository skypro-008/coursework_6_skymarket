from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

from .apps import UsersConfig


app_name = UsersConfig.name

users_router = SimpleRouter()
users_router.register('', UserViewSet, basename='users')

urlpatterns = [
    # Users
    path('', include(users_router.urls)),
]