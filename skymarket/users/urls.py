from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .apps import UsersConfig


# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter
app_name = UsersConfig.name

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")    #в роуте мы регистрируем ViewSet, который импортирован из приложения Djoser

urlpatterns = [
    path("", include(users_router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

